from string import printable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get('https://uk.shop.allpressespresso.com/')
driver.maximize_window()  # zwiekszamy wielkosc okna

time.sleep(1)

cookies = driver.find_element(by=By.XPATH, value='//*[@id="ccc-notify-accept"]')
cookies.click()

descriptions = []

description = driver.find_element(by=By.XPATH, value='//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[1]/div/div/form/div[2]/p').text
descriptions.append(description)

desctiption2 = driver.find_element(by=By.XPATH, value='//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[2]/div/div/form/div[2]/p').text
descriptions.append(desctiption2)

print(descriptions)

driver.quit()


class Scraper():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    
    def get_descriptions(self):
        descriptions = []

        description = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[1]/div/div/form/div[2]/p').text
        descriptions.append(description)

        description2 = driver.find_element_by_xpath('//*[@id="shopify-section-coffee-section"]/div/div/div[2]/div[2]/div/div/form/div[2]/p').text
        descriptions.append(description2)

        return descriptions