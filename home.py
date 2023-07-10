from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element_by_css_selector(".post-160 h3")
book.click()
review = driver.find_element_by_class_name("reviews_tab")
review.click()
yourReview = driver.find_element_by_id("comment")
yourReview.send_keys('Nice book!')
name = driver.find_element_by_id("author")
name.send_keys('Sasha')
email = driver.find_element_by_id("email")
email.send_keys('seventhsky1@rambler.ru')
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()