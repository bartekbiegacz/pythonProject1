from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('nazwa strony' ,driver.title)
time.sleep(3)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
print(button1_accept)
time.sleep(2)


driver.quit()