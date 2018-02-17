#! python3
# sim1.py - Opens all the product pages after searching a shopping site
# such as Amazon.

import requests, sys, webbrowser, bs4

print('Searching Snapdeal...') # display text while downloading snapdeal product page

res = requests.get('''https://www.snapdeal.com/search?keyword=''' + sys.argv[1] + '''&santizedKeyword
	=tishirtfr+man&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&clickSrc=
	go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl
	=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy''')
res.raise_for_status()

# # Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# # Open a browser tab for wach result.
linkElems = soup.select('.product-desc-rating .dp-widget-link')
numOpen = min(2, len(linkElems))
for i in range(numOpen):
	webbrowser.open(linkElems[i].get('href'))