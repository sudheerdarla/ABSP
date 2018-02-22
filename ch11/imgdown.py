#python3
# curretnly this code download only 3-4 images...so have to refactor..
# Edit Code works well and download all the shown images in the webpage.

import requests, sys, webbrowser, bs4, os
from selenium import webdriver

imageList = []
os.makedirs('imgdown', exist_ok = True)
print('Searching Imgur..')
res = requests.get('https://imgur.com/search?q=' + sys.argv[1])
res.raise_for_status()

browser = webdriver.Firefox()
browser.get('https://imgur.com/search?q=' + sys.argv[1])

soup = bs4.BeautifulSoup(res.text, 'html.parser')

imgElems = soup.select('.post .image-list-link')
for i in range(len(imgElems)):
	imgurl = 'https://imgur.com' + imgElems[i].get('href')

	res = requests.get(imgurl)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	finalElems = soup.select('.post-image img')
	if len(finalElems) == 0:
		continue
	else:
		imageList.append('http:' + finalElems[0].get('src'))
	# print(imageList)
	print('Downloading image %s...' % (imageList[-1]))
	res = requests.get(imageList[-1])
	res.raise_for_status()

	for chunk in res.iter_content(100000):
		if len(os.path.basename(imageList[-1])) >= 12:
			continue
		else:
			imageFile = open(os.path.join('imgdown', os.path.basename(imageList[-1])), 'wb')
			imageFile.write(chunk)
	imageFile.close()