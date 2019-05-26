from selenium import webdriver
PATH_TO_DRIVER = 'C:/Users/Henok/Documents/chromedriver/chromedriver.exe'


chrome_options = webdriver.ChromeOptions()
# Disable Info Bar
chrome_options.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path=PATH_TO_DRIVER, chrome_options=chrome_options,)
browser.fullscreen_window()

browser.get('file:///C:/Users/Henok/Documents/FANS/launch/V1/index.html')
