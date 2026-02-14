from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)
upload = driver.find_element(By.ID, 'file-upload')
upload.send_keys("C:/Users/abhij/OneDrive/Pictures/image_1.jpg")
time.sleep(3)
driver.find_element(By.ID, 'file-submit').click()
time.sleep(5)
driver.quit()
