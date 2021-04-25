from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://the-internet.herokuapp.com")

driver.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a').click()

driver.find_element_by_id('username').send_keys("tomsmith")

elem = driver.find_element_by_id('password')
elem.send_keys("SuperSecretPassword!")

driver.find_element_by_xpath('//*[@id="login"]/button/i').click()

print(driver.title)
driver.quit()