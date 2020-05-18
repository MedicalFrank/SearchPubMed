#! python3
# SearchPubmed - opens several pubmed search results

import requests
import sys
import webbrowser
import bs4

print('Searching...') #display text while downloading the search results page
res = requests.get('https://www.ncbi.nlm.nih.gov/pubmed/?term='
                   + ''.join(sys.argv[1:]))
res.raise_for_status()
# User will specfiy the search term using command line arguments when they launch the program.
# Agruments will be stored as strings in a list in sys.argv

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('div.rslt a')

numOpen = min(10, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://www.ncbi.nlm.nih.gov/' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
