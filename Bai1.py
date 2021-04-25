from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")

driver.quit()