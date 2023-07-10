from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
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
sort = driver.find_element_by_css_selector('[value=menu_order]')
sortSel = sort.get_attribute("selected")
assert sortSel == "true"
selector = driver.find_element_by_class_name('orderby')
select = Select(selector)
select.select_by_value("price-desc")
sort = driver.find_element_by_css_selector('[value=price-desc]')
sortSel = sort.get_attribute("selected")
assert sortSel == "true"