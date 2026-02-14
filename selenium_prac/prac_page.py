from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.maximize_window()

driver.get("file:///C:/Users/abhij/PycharmProjects/PythonPractice01/selenium_prac/selenium_prac.html")

fname = driver.find_element(By.ID,"fname")
fname.send_keys("Abhijit")

lname = driver.find_element(By.ID,"lname")
lname.send_keys("Mohanty")

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("abhi@test.com")

gender = driver.find_element(By.CSS_SELECTOR,"input[type='radio']")
gender.click()

mobile = driver.find_element(By.XPATH, "//input[@id='mobile']")
mobile.send_keys(7325903082)

dob = driver.find_element(By.XPATH, "//input[@type='date']")
dob.send_keys("10-02-1999")

hobbies = driver.find_element(By.XPATH, "//input[@type='checkbox']")
hobbies.click()

country = driver.find_element(By.XPATH,"//option[text()='Brazil']").click()

# alert = driver.switch_to.alert
# alert.accept()

# country = driver.find_element(By.XPATH, "//datalist[@id='countryList']/option")/

time.sleep(3)
driver.quit()