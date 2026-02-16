from playwright.sync_api import sync_playwright
import time

with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    print(page.title())
    time.sleep(2)

    page.fill("#name","Abhijit")

    page.once("dialog", lambda dialog:(
        print("ALERT TEXT:-", dialog.message),
        dialog.accept()
    ))
    time.sleep(2)

    page.click("#alertbtn")
    time.sleep(2)
    browser.close()