import requests, bs4, webbrowser 
res = requests.get('https://sudheerdarla.github.io/')
res.raise_for_status()
netest = bs4.BeautifulSoup(res.text,  'html.parser')
# print(res.text)
for link in netest.find_all('a'):
	webbrowser.open(link.get('href'))