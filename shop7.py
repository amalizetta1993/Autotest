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
driver.execute_script("window.scrollBy(0, 300);")
add = driver.find_element_by_css_selector('[data-product_id="182"]')
add.click()
time.sleep(5)
bucket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
bucket.click()
time.sleep(5)
proceed = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".alt.wc-forward")))
proceed = driver.find_element_by_css_selector(".alt.wc-forward")
proceed.click()
firstName = driver.find_element_by_id('billing_first_name')
firstName.send_keys('Sasha')
lastName = driver.find_element_by_id('billing_last_name')
lastName.send_keys('Kamchenkova')
email = driver.find_element_by_id('billing_email')
email.send_keys('seventhsky1@rambler.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('+76266256526')
adres = driver.find_element_by_id('billing_address_1')
adres.send_keys('Ryazan')
town = driver.find_element_by_id('billing_city')
town.send_keys('Ryazan')
country = driver.find_element_by_id('select2-chosen-1')
country.click()
country2 = driver.find_element_by_id('s2id_autogen1_search')
country2.send_keys('Russia')
country3 = driver.find_element_by_id('select2-results-1')
country3.click()
time.sleep(2)
state = driver.find_element_by_id('billing_state')
state.send_keys('Ryazan')
zip = driver.find_element_by_id('billing_postcode')
zip.send_keys('455454')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_id('payment_method_cheque')
pay.click()
place = driver.find_element_by_id('place_order')
place.click()
some_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order_details .method"), "Check Payments"))