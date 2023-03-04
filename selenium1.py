from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('nazwa strony' ,driver.title)
time.sleep(3)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
print(button1_accept)
search_field = driver.find_element('name', 'q')
search_field.send_keys('czy jutro jest niedziela handlowa?')
#search_field.send_keys(keys.enter)
search_button = driver.find_element('name', 'btnK')
search_button.submit()
time.sleep(3)
driver.quit()


driver.quit()