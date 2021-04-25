from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

driver.get("http://practice.automationtesting.in/")
print(driver.title)

driver.quit()