from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Edge()
driver.maximize_window()
driver.get("file:///C:/Users/abhij/PycharmProjects/PythonPractice01/selenium_prac/full_automation.html")

name = driver.find_element(By.ID, 'name')
name.send_keys("Abhijit Mohanty")
time.sleep(2)

gender = driver.find_element(By.XPATH,"(//input[@name='gender'])[1]").click()
time.sleep(2)

skill = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in skill:
    checkbox.click()
time.sleep(2)

count = driver.find_element(By.XPATH, "//select[@id='country']")
dropd = Select(count)
dropd.select_by_index(2)
time.sleep(2)

auto_suggests = driver.find_element(By.ID, "country_suggest")
auto_suggests.send_keys("us")
suggesterd_country = driver.find_elements(By.XPATH,"//ul[@id='suggestions']/li")
for countrys in suggesterd_country:
    if "USA" == countrys.text:
        countrys.click()
time.sleep(2)

dob = driver.find_element(By.XPATH,"//input[@id='dob']")
dob.send_keys("10-02-2023")
time.sleep(2)

mmt = driver.find_element(By.XPATH,"(//div[text()='2'])[1]")
mmt.click()
time.sleep(2)

upload = driver.find_element(By.ID,"fileUpload")
upload.send_keys("C:/Users/abhij/OneDrive/Pictures/image_1.jpg")
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(2)


new_tab = driver.find_element(By.XPATH,"//button[text()='Open New Tab']").click()
time.sleep(2)

# new_window = driver.find_element(By.XPATH,"//button[text()='Open New Window']").click()

wait = WebDriverWait(driver,4)
driver.find_element(By.XPATH, "//button[text()='Alert']").click()
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.accept()
time.sleep(2)

wait1 = WebDriverWait(driver,3)
driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
alert1 = wait1.until(EC.alert_is_present())
alert.accept()
time.sleep(2)

wait2 = WebDriverWait(driver,3)
driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
alert2 = wait1.until(EC.alert_is_present())
alert2.send_keys("Hey I am Abhi")
alert.accept()
time.sleep(2)

mouse_hover = driver.find_element(By.CLASS_NAME,'hover-box')
action = ActionChains(driver)
action.move_to_element(mouse_hover).perform()
print(mouse_hover.text)
time.sleep(2)

option1 = driver.find_element(By.XPATH, "//button[text()='Option 1']")
time.sleep(2)

double_click = driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
action2 = ActionChains(driver)
action2.double_click(double_click).perform()
wait2 = WebDriverWait(driver,4)
double_click = wait2.until(EC.alert_is_present())
alert.accept()
time.sleep(4)

source = driver.find_element(By.ID,"drag")
target = driver.find_element(By.ID,"drop")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(5)

right_click = driver.find_element(By.ID,"rightClickBox")
action = ActionChains(driver)
action.context_click(right_click).perform()
time.sleep(2)

edit = driver.find_element(By.XPATH,"//button[text()='Edit']")
edit.click()
wait4 = WebDriverWait(driver,3)
edit = wait4.until(EC.alert_is_present())
alert.accept()

frame = driver.find_element(By.ID,"frame1")
driver.switch_to.frame("frame1")
click_inside = driver.find_element(By.ID,"btn1")
click_inside.click()
driver.switch_to.default_content()
time.sleep(2)

keyword = driver.find_element(By.ID, "keyboardField1")
keyword.send_keys("Abhijit Mohanty")
keyword.send_keys(Keys.CONTROL+'a')
keyword.send_keys(Keys.CONTROL+'c')

keywords = driver.find_element(By.ID,'keyboardField2')
keywords.send_keys(Keys.CONTROL+'v')
time.sleep(3)

submit = driver.find_element(By.XPATH,"//button[text()='Submit']")
submit.click()

time.sleep(3)
driver.quit()