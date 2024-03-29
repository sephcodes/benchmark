import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

# set up the driver
browser = webdriver.Chrome()

url = "https://humanbenchmark.com/tests/typing"
browser.get(url)

# give some time for page to fully load
time.sleep(4)

# get the page source
page_source = browser.page_source

# use beautifulsoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('span', class_='incomplete')
text_to_type = ''.join([span.get_text() for span in spans])
print(text_to_type)

# wait for a short moment to ensure the webpage is focused
time.sleep(2)

# type the text using pyautogui
pyautogui.write(text_to_type, interval=0)
pyautogui.press('enter')

# add input to terminal to keep command running and not quit browser
input("Press Enter to close the browser...")