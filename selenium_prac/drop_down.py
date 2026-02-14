from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

dropdown_ele = driver.find_element(By.ID,"dropdown-class-example")
drpdwn = Select(dropdown_ele)
# drpdwn.select_by_value('option1')
#By index position
drpdwn.select_by_index(2)
#By Visible text
# drpdwn.select_by_visible_text("Option1")
time.sleep(3)
driver.quit()