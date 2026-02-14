from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

driver.execute_script('window.scrollBy(0,900);')
time.sleep(2)

mouse_hover = driver.find_element(By.ID,'mousehover')
action = ActionChains(driver)
action.move_to_element(mouse_hover).perform()

reload = driver.find_element(By.LINK_TEXT, 'Reload')
reload.click()

time.sleep(3)
driver.quit()