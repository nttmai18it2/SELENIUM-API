from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id('menu-item-50').click()

driver.find_element_by_id('reg_email').send_keys("ttmphuong@gmail.com")

elem = driver.find_element_by_id('reg_password')
elem.send_keys("p0342048971")

driver.find_element_by_class_name('register').click()

driver.quit()