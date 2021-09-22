import urllib.request
import os
import random
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool

###################################################################################

path = "pics\\"

NO_OF_THREADS=1

base_url = 'https://www.imdb.com'
TITLES_LIST_FILE='movie-titles.txt'

###################################################################################
def get_title_webpage(title_id):
    """Given an IMDb title_id this function will return the title's webpage as
    a BeautifulSoup object."""

    # Construct base_url + u/
    title_url = base_url + '/title/' + title_id

    # Get the HTML of the title's IMDb page
    html = urlopen(title_url)

    # Create a BeautifulSoup object
    bs = BeautifulSoup(html,"html.parser")

    return bs

def get_title_poster_webpage(bs):
    """Given a BeautifulSoup object of a title's IMDb webpage this function will     return the url for its poster."""

    # Extract poster link
    data = bs.find('a',{'class':'ipc-lockup-overlay'})
    poster_link = data.get('href')

    # Construct url for title
    title_url = base_url + '/' + poster_link
    # Get the HTML of the title's IMDb page
    html = urlopen(title_url)
    # Create a BeautifulSoup object
    bs = BeautifulSoup(html,"html.parser")

    return bs 
  
 
def get_title_poster_url(bs):
    """Given a BeautifulSoup object of a title's IMDb webpage this function will
    return the url for its poster."""

    # Extract poster link
    data = bs.find('img',{'class':'MediaViewerImagestyles__PortraitImage-sc-1qk433p-0'})
    poster_link = data.get('src')

    return poster_link

def save_image(file_name, image_link):
    #print("Entering into save_image:", image_link )

    s = os.path.join(path, file_name)
    print("[{0}] - Saving to : {1}".format(file_name,s))
    output = open(s,'wb')
    resource_img = urllib.request.urlopen(image_link)
    data = resource_img.read()
    output.write(data)
    output.close()

def sleeper():
    val = random.randint(1,5)
    print("Sleeping for [{0}] seconds".format(val))
    time.sleep(val)

def title_orchestrator(title_id):
    print("Processing:", title_id)

    sleeper()
    retVal = get_title_webpage(title_id)
    
    sleeper()
    retVal = get_title_poster_webpage(retVal)

    sleeper()
    retVal = get_title_poster_url(retVal)

    sleeper()
    save_image('poster-' + title_id + ".jpg", retVal)

    sleeper()

def init_data():
    arr_of_titles = []

    with open(TITLES_LIST_FILE) as file:
        for line in file:
            arr_of_titles.append(line)

    print("Total Titles are :", len(arr_of_titles) )

    return ['tt0165362', 'tt0034583','tt0035423','tt0037445']
    #return arr_of_titles

def start_processing():    
    arr_of_titles=init_data() 
        
    pool = ThreadPool(NO_OF_THREADS)
    results = pool.map(title_orchestrator, arr_of_titles)

    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join() 

    for itr in results:
        print(itr)
    
#########################################################################

if __name__ == "__main__":
    start_processing()
