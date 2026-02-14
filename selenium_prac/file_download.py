from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import os

download_dir = "D:/Downloads"

edge_options = Options()

pref = {
"download.default_directory":download_dir,
"download.prompt_for_download":False,
"directory_upgrade": True
}
edge_options.add_experimental_option("prefs",pref)
driver=webdriver.Edge(options=edge_options)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(3)

driver.find_element(By.LINK_TEXT,'random_data.txt').click()
time.sleep(2)

file_path=os.path.join(download_dir)
print('downloaded:',os.path.exists(file_path))
time.sleep(7)

driver.quit()