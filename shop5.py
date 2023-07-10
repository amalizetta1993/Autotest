from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
time.sleep(5)
add = driver.find_element_by_css_selector('[data-product_id="182"]')
add.click()
time.sleep(5)
buck = driver.find_element_by_class_name('cartcontents')
print(str(buck.text))
assert str(buck.text) == "1 Item"
buckSum = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
assert str(buckSum.text) == "₹180.00"
bucket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
bucket.click()
subTotal = WebDriverWait(driver, 20).until_not(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount")))
Total = WebDriverWait(driver, 20).until_not(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount")))