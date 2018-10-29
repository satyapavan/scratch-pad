import urllib.request
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.santabanta.com/images/parent/2/'

# query the website and return the html to the variable 'page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

print(name_box);
name = name_box.text.strip() # strip() is used to remove starting and trailing print name

