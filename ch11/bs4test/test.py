from bs4 import BeautifulSoup
doc = open('doc.html')
soup = BeautifulSoup(doc, 'html.parser')

# print(soup.prettify())
for link in soup.find_all('a'):
	print(link.get('href'))