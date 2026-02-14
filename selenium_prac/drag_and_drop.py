from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))
source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

time.sleep(3)
driver.quit()