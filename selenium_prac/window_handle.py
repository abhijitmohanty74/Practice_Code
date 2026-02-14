from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.execute_script('window.scrollBy(0,900);')
time.sleep(3)

parent_window= driver.current_window_handle
print('Parent window:',parent_window)

driver.find_element(By.ID,'openwindow').click()
time.sleep(2)

all_windows=driver.window_handles
print(all_windows)

for window in all_windows:
    if window!=parent_window:
        driver.switch_to.window(window)
        break
print('child window titles:',driver.title)

driver.find_element(By.LINK_TEXT,'Courses').click()
time.sleep(3)
driver.close()

driver.switch_to.window(parent_window)
time.sleep(2)
driver.quit()