import urllib.request
import os
from bs4 import BeautifulSoup
            
def save_image(image_link):
            print("Entering into save_image:", image_link )
            c = image_link.split('/')[-1]
            s=c
            s = os.path.join(path, s)
            print("Saving {0} to location : {1}".format(c,s))
            output = open(s,'wb')
            resource_img = urllib.request.urlopen(image_link)
            data = resource_img.read()
            output.write(data)
            output.close()

def download_celeb(url):
    print("Entering into download_celeb:",  url)
    page_no=1
    url = url + '?page='
    print(url + str(page_no))
    while (page_no <= MAX_NUMBER_OF_PAGES):
        resource_celeb = urllib.request.urlopen(url + str(page_no))
        celeb_soup = BeautifulSoup(resource_celeb, 'html.parser')
        #print(celeb_soup)
        for link in celeb_soup.select('div .imgdiv1 > a'):
            #print(link)
            image_link = link.find('img').get('src')
            print("", image_link)
            save_image(image_link)

            width = link.find('img').get('width')
            height = link.find('img').get('height')
            desc = link.find('img').get('alt')
            
        page_no = page_no + 1
    
def downloader(soup):
    print("Entering into downloader....")
    for link in soup.select('div .imgdiv1 > a'):
        celeb_href=link.get('href')
        celeb_name=link.find('img').get('alt')
        print(celeb_href, celeb_name);
        download_celeb(base_url + celeb_href);


#########################################################################
path = "H:\\coding\\git\\scratch-pad\\"

# specify the url
MAX_NUMBER_OF_PAGES=2
base_url = 'http://www.santabanta.com'
quote_page = 'http://www.santabanta.com/images/parent/2/'
#quote_page = 'http://www.santabanta.com/photos/birds/2112292.htm'

# query the website and return the html to the variable 'page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


# Take out the <div> of name and get its value
#name_box = soup.find('h1', attrs={'class': 'name'})

#name = name_box.text.strip() # strip() is used to remove starting and trailing print name

downloader(soup)
