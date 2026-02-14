from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# check_box = driver.find_element(By.ID,"checkBoxOption1")
# check_box1 = driver.find_element(By.ID, "checkBoxOption2")
# check_box2 = driver.find_element(By.ID, "checkBoxOption3")
#
# check_box.click()
# check_box1.click()
# check_box2.click()

# Find By XPath
check_boxes = driver.find_elements(By.XPATH, "//input[contains(@id,'checkBoxOption')]")
for box in check_boxes:
    box.click()

time.sleep(3)
driver.quit()