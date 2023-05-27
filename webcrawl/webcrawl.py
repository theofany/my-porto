from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
import time
import pandas as pd

# driver = webdriver.Chrome('chromedriver.exe')
# url ="https://www.nasa.gov/multimedia/imagegallery/iotd.html"
# driver.get(url)
# images = driver.find_elements(By.XPATH,'<div class="image"> <img src="/sites/default/files/styles/image_card_4x3_ratio/public/thumbnails/image/afrc2022-0025-003large.jpg" alt="F/A-18E in Hanger.">')
# for image in images:
#     print(images.get_attribute("src"))
#     driver.close()


search = "nasa"
page = 2
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://google.com')
driver.find_element(By.NAME, "q").send_keys(search + Keys.ENTER)
more = driver.find_element(By.TAG_NAME, "g-more-link")
more_btn = more.find_element(By.TAG_NAME, "a")
more_btn.click()
time.sleep(100)