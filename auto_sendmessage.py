from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the web driver
chrome_browser = webdriver.Chrome(options= chrome_options)
chrome_browser.get('https://web.archive.org/web/20230608193521/http://demo.seleniumeasy.com/basic-first-form-demo.html')



user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys("I AM EXTRA COLL") #TO mimic typing into message bbox


# print('Selenium Easy - Checkbox demo for automation using selenium' in chrome_browser.title)
print(chrome_browser)



