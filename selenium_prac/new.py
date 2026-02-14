from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("file:///C:/Users/abhij/PycharmProjects/PythonPractice01/selenium_prac/full_automation.html")

source = driver.find_element(By.ID,"drag")
target = driver.find_element(By.ID,"drop")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(5)


keyword = driver.find_element(By.ID, "keyboardField1")
keyword.send_keys("Abhijit Mohanty")
keyword.send_keys(Keys.CONTROL+'a')
keyword.send_keys(Keys.CONTROL+'c')

keywords = driver.find_element(By.ID,'keyboardField2')
keywords.send_keys(Keys.CONTROL+'v')
time.sleep(3)