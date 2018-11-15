import urllib.request
import os
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

###################################################################################

path = "pics\\"

PAGE_DEPTH_PER_CELEB=15
PAGE_DEPTH=5
NO_OF_THREADS=5

base_url = 'http://www.santabanta.com'
gallary_page = 'http://www.santabanta.com/images/parent/2/?page='
#quote_page = 'http://www.santabanta.com/photos/birds/2112292.htm'

###################################################################################

def save_image(celeb_name, image_link):
    #print("Entering into save_image:", image_link )
    c = image_link.split('/')[-1]
    s=c
    s = os.path.join(path, celeb_name, s)
    print("[{0}] - Saving to : {1}".format(celeb_name,s))
    output = open(s,'wb')
    resource_img = urllib.request.urlopen(image_link)
    data = resource_img.read()
    output.write(data)
    output.close()

def download_celeb(celeb_name, url):
    print("Entering into download_celeb:",  celeb_name, url)
    image_count=0
    page_no=1
    url = url + '?page='
    #print(url + str(page_no))

    # Create directory for the celeb and then start downloading
    os.mkdir(os.path.join(path, celeb_name))
    
    while (page_no <= PAGE_DEPTH_PER_CELEB):
        resource_celeb = urllib.request.urlopen(url + str(page_no))
        celeb_soup = BeautifulSoup(resource_celeb, 'html.parser')
        #print(celeb_soup)
        for link in celeb_soup.select('div .imgdiv1 > a'):
            #print(link)
            image_link = link.find('img').get('src')
            #print("", image_link)
            save_image(celeb_name, image_link)

            image_count = image_count + 1
            width = link.find('img').get('width')
            height = link.find('img').get('height')
            desc = link.find('img').get('alt')
            
        page_no = page_no + 1

    return celeb_name + '  --  ' + str(image_count)

def download_celeb_top(param):
    print("Downloading celeb:", param)
    token=param.split('|')

    if( len(token) == 2):
        print
        return download_celeb(token[0], base_url + token[1])
    
def fetch_celebs_in_a_page(soup):
    print("Entering into downloader....")

    ret_val = []
    for link in soup.select('div .imgdiv1 > a'):
        celeb_href=link.get('href')
        celeb_name=link.find('img').get('alt')
        celeb_name=(celeb_name.replace(' ', '-')).lower()        
        print(celeb_name, celeb_href );
        ret_val.append(celeb_name + '|' + celeb_href)
    return ret_val

def fetch_all_pages():
    page_no=1
    arr_of_celebs = []
    while (page_no <= PAGE_DEPTH):    
        url = gallary_page + str(page_no)
        print(url)
        
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        arr_of_celebs.extend(fetch_celebs_in_a_page(soup))

        page_no = page_no + 1

    print(arr_of_celebs)
    return arr_of_celebs
    
def start_processing():    
    arr_of_celebs=fetch_all_pages()
    
    pool = ThreadPool(NO_OF_THREADS)
    results = pool.map(download_celeb_top, arr_of_celebs)

    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join() 

    for itr in results:
        print(itr)
    
#########################################################################

if __name__ == "__main__":
    start_processing()
