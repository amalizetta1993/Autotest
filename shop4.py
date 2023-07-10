from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50")
account.click()
login = driver.find_element_by_id("username")
login.send_keys('seventhsky1@rambler.ru')
passwordReg = driver.find_element_by_id("password")
passwordReg.send_keys('Pasha1122!')
loginBtn = driver.find_element_by_name("login")
loginBtn.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
time.sleep(5)
book = driver.find_element_by_partial_link_text("Android Quick Start Guide")
book.click()
price = driver.find_element_by_css_selector("del .woocommerce-Price-amount.amount")
assert str(price.text)== "₹600.00"
priceNew = driver.find_element_by_css_selector("ins .woocommerce-Price-amount.amount")
assert str(priceNew.text)== "₹450.00"
img = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")))
img=driver.find_element_by_css_selector(".woocommerce-main-image.zoom")
img.click()
img1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
img1=driver.find_element_by_class_name("pp_close")
img1.click()