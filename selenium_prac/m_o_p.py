from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- Browser setup ----------
driver = webdriver.Edge()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# ---------- Open Flipkart ----------
driver.get("https://www.flipkart.com")

# ---------- Close login popup ----------
try:
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='✕']"))
    )
    close_btn.click()
except:
    pass  # popup may not appear every time

# ---------- Locate Fashion menu ----------
fashion = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Fashion']")
    )
)

actions = ActionChains(driver)

# ---------- Hover on Fashion ----------
actions.move_to_element(fashion).perform()
time.sleep(1)

# ---------- Hover on Men ----------
men = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[text()='Men']")
    )
)
actions.move_to_element(men).perform()
time.sleep(5)

# ---------- Click on Footwear ----------
footwear = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Footwear')]")
    )
)

actions.move_to_element(footwear).click().perform()

time.sleep(9)
driver.quit()