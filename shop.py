import time
from selenium import webdriver
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
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
book = driver.find_element_by_css_selector(".post-181 h3")
book.click()
header=driver.find_element_by_css_selector(".summary.entry-summary>h1")
element_get_text = header.text
assert element_get_text == "HTML5 Forms"
driver.quit()


from selenium import webdriver
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
html = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]')
html.click()
numbers = driver.find_elements_by_class_name("product-type-simple")
(len(numbers)) ==3
driver.quit()