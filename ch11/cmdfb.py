from selenium import webdriver
import time 

browser = webdriver.Firefox()
browser.get('https://fb.com')

print('Login into your Fecabook!')

username = input('Username: ')
mailElem = browser.find_element_by_id('email')
mailElem.send_keys(username)

password = input('Password: ')
passElem = browser.find_element_by_id('pass')
passElem.send_keys(password)
passElem.submit()
time.sleep(4)

# message will be sent to the first contact in your message box
browser.get('https://www.facebook.com/messages') 
time.sleep(3)
msgElem = browser.find_element_by_class_name('notranslate')
msgElem.send_keys("Yo!")

# text is case sensitive
sendElem = browser.find_element_by_link_text('Send')
sendElem.click()
print('Newsfeed in 5 seconds..')
time.sleep(5)
browser.back()