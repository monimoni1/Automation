from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


chrome_browser= webdriver.Chrome(options=chrome_options)
# chrome_browser.maximize_window()

print(chrome_browser)