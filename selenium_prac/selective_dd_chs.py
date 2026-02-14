from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

selective_dd = Select(driver.find_element(By.ID, 'dropdown-class-example'))
selective_dd.select_by_index(2)

time.sleep(3)
driver.quit()