from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import time

search = "landscaping in dallas"

pages = 2
header = ["data_cid", "title", "category", "description"]
data = []
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.headless = True
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com')
driver.implicitly_wait(2)
driver.find_element(By.NAME, "q").send_keys(search + Keys.ENTER)
more = driver.find_element(By.TAG_NAME, "g-more-link")
more_btn = more.find_element(By.TAG_NAME, "a")
more_btn.click()
time.sleep(10)
for page in range(2, pages + 1):
    elements = driver.find_elements(By.CSS_SELECTOR,
                                    'div#search a[class="vwVdIc wzN8Ac rllt__link a-no-hover-decoration"')
    counter = 1
    for element in elements:
        data_cid = element.get_attribute('data-cid')
        element.click()
        print('item click... 5 seconds...')
        time.sleep(5)
        # title
        title = driver.find_element(By.CSS_SELECTOR, 'h2[data-attrid="title"]')
        print('title: ', title.text)
        # category
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR,
                                           'div[data-attrid="kc:/local:lu attribute list"] > div > div > span')
            if len(temp_obj.text) > 0:
                category = temp_obj.text
        except NoSuchElementException:
            try:
                temp_obj = driver.find_element(By.CSS_SELECTOR,
                                               'div[data-attrid="kc:/local:one line summary"] > div > span')
                if len(temp_obj.text) > 0:
                    category = temp_obj.text
            except NoSuchElementException:
                category = ""
        print('category:', category)
        # description
        try:
            temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-long-text]')
            if len(temp_obj.get_attribute('data-long-text')) > 0:
                description = temp_obj.get_attribute('data-long-text')
        except NoSuchElementException:
            '''
            try:
                temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/local:merchant_description"] > c-wiz > div > div:nth-child(2)')
                if len(temp_obj.get_attribute('innerHTML')) > 0:
                    description = temp_obj.get_attribute('innerHTML')
            except NoSuchElementException:
                description =""
            '''
            description = ""

        print('description:', description)
        row = [data_cid, title.text, category, description]
        data.append(row)
        counter += 1
    try:
        page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Page ' + str(page) + '"]')
        page_button.click()
        print('page click... 10 seconds...')
        time.sleep(10)
    except NoSuchElementException:
        break
with open('gmap.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)