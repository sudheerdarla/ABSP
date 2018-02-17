#! python3
# backupweb.py - Backups an entire site by following all of its links.

import requests, bs4, os, webbrowser, pprint

# Download the home page of the given link
url = 'https://automatetheboringstuff.com/'
os.makedirs('auto', exist_ok = True)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())
# site = soup.select('a')

# sitefile = open('auto/home.html', 'wb')
# for chunk in res.iter_content(100000):
# 	sitefile.write(chunk)
# sitefile.close()

# pprint.pprint(elems)

# for i in range(len(site)):
# 	print(site[i].get('href'))
# When link clicked take me to the that specific html page that saved already


# First I am going to save only the links that are avaialable in the home
## page that I have given