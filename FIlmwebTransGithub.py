from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#variables
n=1242 #length of the list


f=open("input.txt", 'r')
o=open("out.txt", 'w+')

#setting the variable 'pom' for future checking
my_url='https://www.filmweb.pl/films/search?q=Godfather'
uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup= soup(page_html, 'html.parser')
pom=page_soup.find('div', class_='section__description')


for j in range(n):
    #making the url
    a=f.readline()
    inp=a.replace('\n', '')
    debug=inp
    key=(inp.replace(' ', '+'))
    my_url='https://www.filmweb.pl/films/search?q='+key
    print(my_url)

    #downloading the page
    uClient = uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup= soup(page_html, 'html.parser')

    #searching for a film with searched title
    tab=page_soup.find_all('div', class_="filmPreview__originalTitle")
    index=-1
    if(pom!=page_soup.find('div', class_='section__description')):
        o.write(inp)
        debug+=' :   '+inp
    else:
        for i in range(len(tab)):
            if tab[i].string.lower()==inp.lower():
                pomoc=tab[i].parent
                pomoc=pomoc.div
                pomoc=pomoc.a
                pomoc=pomoc.h3
                index=1
                try: #trying to get the polish title if program found the english one
                    debug+=' :   '+pomoc.string
                    o.write(pomoc.string)
                except:
                    debug+=' :   '+inp
                    o.write(inp)
                break
        if index==-1: #when it didnt find that film it will return the english title
            debug+=' :   '+inp
            o.write(inp)
    o.write("\n")
    print(debug)
o.close()
