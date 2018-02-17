from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://mail.google.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.clear()
mail = input('Enter your mail: ')
emailElem.send_keys(mail)
nextElem = browser.find_element_by_class_name('RveJvd')
nextElem.click()
time.sleep(2)
passElem = browser.find_element_by_class_name('whsOnd')
password = input('Enter your password: ')
passElem.send_keys(password)
nextElem = browser.find_element_by_class_name('RveJvd')
nextElem.click()
time.sleep(5)
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')


# mail compsing ------ this section not working, because mail.google.com
# changes the ids and class names everytime we refresh or login, so needs
# different aproach if at all google allows.
# -----------------------
# toElem = browser.find_element_by_id(':ug')
# toElem.send_keys('sudheer.darla11@gmail.com')
# subElem = browser.find_element_by_id(':u6')
# subElem.send_keys('Test from CMD line Emailer!')
# textElem = browser.find_element_by_id(':v9')
# textElem.send_keys('Hello, Sud!')
# sendElem = browser.find_element_by_id(':tv')
# sendElem.click()


# compose class - T-I J-J5-Ji
# To: id        - :ug
# Subject: id   - :u6 
# mailtext: id  - :v9
# send: id      - :tv 