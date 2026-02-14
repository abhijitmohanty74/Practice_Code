from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
time.sleep(3)

double_click = driver.find_element(By.ID,'doubleClickBtn')
action = ActionChains(driver)
action.double_click(double_click).perform()
print(double_click.is_enabled())
time.sleep(3)
driver.quit()