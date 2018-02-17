#! python3
# sim3.py - Open the result links to photos after performing a search
# on a photo site sucha as Flickr or Imgur

import requests, sys, webbrowser, bs4

print('Searching Imgur..')
res = requests.get('''https://imgur.com/search?q=''' + sys.argv[1])
res.raise_for_status()

# # Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.post .image-list-link')

numOpen = min(2, len(linkElems))
for i in range(numOpen):
	webbrowser.open('https://imgur.com' + linkElems[i].get('href'))
