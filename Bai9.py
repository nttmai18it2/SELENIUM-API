from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://itmscoaching.herokuapp.com/form")

driver.find_element_by_id('first-name').send_keys("Binh")
driver.find_element_by_id('last-name').send_keys("Nguyen")
driver.find_element_by_id('job-title').send_keys("Tester")
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()
driver.find_element_by_css_selector("#select-menu [value='1']").click()
driver.find_element_by_id('datepicker').send_keys("04/01/2000")

driver.find_element_by_xpath('/html/body/div/form/div/div[8]/a').click()

driver.quit()