from urllib.request import urlopen as u
from bs4 import BeautifulSoup as bs

my_url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

#open the connection and get the page with the above URL
uClient = u(my_url)
page_html = uClient.read()   # HTML content 
uClient.close()

#parse the HTML content
pageContent = bs(page_html,"html.parser")
print(pageContent.h1)
print(pageContent.p)
count = pageContent.findAll("div")
print("Count is: len(count)")
print(count[0])