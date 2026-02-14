from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(3)

name = driver.find_element(By.ID,'userName')
name.send_keys('Abhijit Mohanty')

name.send_keys(Keys.CONTROL+'a')
name.send_keys(Keys.CONTROL+'c')

email = driver.find_element(By.ID,'userEmail')
email.send_keys(Keys.CONTROL+'v')
# driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))
# source = driver.find_element(By.ID,'draggable')
# target = driver.find_element(By.ID,'droppable')
#
# action = ActionChains(driver)
# action.drag_and_drop(source, target).perform()

time.sleep(3)
driver.quit()