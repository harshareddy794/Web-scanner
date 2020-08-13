from bs4 import BeautifulSoup
import urllib.request,urllib.error,urllib.parse
def crawler(url):
    if(len(url)==0):
        return 'Enter a valid link' 
    try:
        links=[]
        # Sending request to server using BeautifulSoup
        html_data=urllib.request.urlopen(url).read()
        
        #Beautyfying all data to html form 
        soup=BeautifulSoup(html_data,'html.parser')

        #Retriving all anchor tags in html data
        tags=soup('a')

        #Adding all href attribute values to list
        for tag in tags:
                if tag.has_attr('href'):
                    links.append(tag['href'])
        print(links)
        return 'No error'
    except:
        #Check if any errors
        return 'Please check the URL properly' 
