from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element(By.NAME, "fName")
first_name.send_keys("Ali")
last_name=driver.find_element(By.NAME, "lName")
last_name.send_keys("Khan")
email=driver.find_element(By.NAME, "email")
email.send_keys("alikhan@gmail.com")
submit=driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

#article_count=driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
#print(article_count.text)

