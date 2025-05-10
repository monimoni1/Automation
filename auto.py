from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# creating an instance of the web driver
chrome_browser = webdriver.Chrome(options= chrome_options)
chrome_browser.get('http://web.archive.org/web/20230608194415/http://demo.seleniumeasy.com/basic-checkbox-demo.html')

assert 'Show message' in  chrome_browser.page_source

print('Selenium Easy - Checkbox demo for automation using selenium' in chrome_browser.title)
print(chrome_browser)

