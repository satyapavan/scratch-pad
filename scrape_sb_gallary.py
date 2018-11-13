import urllib.request
import os
from bs4 import BeautifulSoup
            
def save_image(celeb_name, image_link):
            print("Entering into save_image:", image_link )
            c = image_link.split('/')[-1]
            s=c
            s = os.path.join(path, celeb_name, s)
            print("Saving {0} to location : {1}".format(c,s))
            output = open(s,'wb')
            resource_img = urllib.request.urlopen(image_link)
            data = resource_img.read()
            output.write(data)
            output.close()

def download_celeb(celeb_name, url):
    print("Entering into download_celeb:",  url)
    page_no=1
    url = url + '?page='
    print(url + str(page_no))
    while (page_no <= PAGE_DEPTH):
        resource_celeb = urllib.request.urlopen(url + str(page_no))
        celeb_soup = BeautifulSoup(resource_celeb, 'html.parser')
        #print(celeb_soup)
        for link in celeb_soup.select('div .imgdiv1 > a'):
            #print(link)
            image_link = link.find('img').get('src')
            print("", image_link)
            save_image(celeb_name, image_link)

            width = link.find('img').get('width')
            height = link.find('img').get('height')
            desc = link.find('img').get('alt')
            
        page_no = page_no + 1
    
def downloader(soup):
    print("Entering into downloader....")
    for link in soup.select('div .imgdiv1 > a'):
        celeb_href=link.get('href')
        celeb_name=link.find('img').get('alt')
        celeb_name=(celeb_name.replace(' ', '-')).lower()        
        print(celeb_href, celeb_name);
        os.mkdir(os.path.join(path, celeb_name))
        download_celeb(celeb_name, base_url + celeb_href);


#########################################################################
path = "H:\\coding\\git\\scratch-pad\\pics\\"

# specify the url
PAGE_DEPTH=15

base_url = 'http://www.santabanta.com'
gallary_page = 'http://www.santabanta.com/images/parent/2/?page='
#quote_page = 'http://www.santabanta.com/photos/birds/2112292.htm'

page_no=1
url = gallary_page + str(page_no)
print(url)
while (page_no <= 5):    
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    downloader(soup)

    page_no = page_no + 1
