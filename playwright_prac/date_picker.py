from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# text = driver.find_element(By.ID,"name")
# text.send_keys("Abhi")
dropdown_ele = driver.find_element(By.ID,"dropdown-class-example")
drpdwn = Select(dropdown_ele)
drpdwn.select_by_value('option1')
time.sleep(3)
driver.quit()