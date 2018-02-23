#! python3
# linkverif.py - Write a program that, given the URL of a web page, 
# will attempt to download every linked page on the page.
# The program should flag any pages that have a 404 “Not Found” status
# code and print them out as broken links.

from selenium import webdriver
import bs4, requests

# parse a website link and save all the links to a list
link = str(input("Enter Link: "))

res = requests.get(link)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

allLinks = soup.select('a')
links = []
for i in range(len(allLinks)):
	if str(allLinks[i].get('href')).startswith('http'):
		allLinks[i] = allLinks[i].get('href')
	else:
		allLinks[i] = link + allLinks[i].get('href')

	links.append(allLinks[i])

links.append(link + '/sdf') # adding a broken link to test
WL = [] # Working Links
BL = [] # Broken Links
# look for status code and prompt according it.
for i in range(len(links)):
	res = requests.get(links[i])
	if res.status_code != 404:
		print(links[i] + ' (this link WORKS!)')
		WL.append(links[i])
	if res.status_code == 404:
		print(links[i] + ' (BROKEN! Error 404)')
		BL.append(links[i])

print('----------SUMMARY-----------')
print('Total links in this page: {}'.format(len(links)))
print('Total Working Links: {}'.format(len(WL)))
print('Total Broken Links: {}'.format(len(BL)))
print(BL)