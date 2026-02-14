from playwright.sync_api import sync_playwright
import time


with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(r"C:/Users/abhij/PycharmProjects/PythonPractice01/playwright_prac/playwright_prac.html")
    print(page.title())

    page.select_option("select", label="South Africa")

    time.sleep(3)
    browser.close()