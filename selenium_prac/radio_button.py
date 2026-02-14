from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = driver.find_element(By.ID, "name").send_keys("Satya")

# rdo = driver.find_element(By.NAME, "radioButton")


# rdo.click()


time.sleep(3)
driver.quit()