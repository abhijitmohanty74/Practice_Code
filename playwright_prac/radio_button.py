from playwright.sync_api import sync_playwright
import time


with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(r"C:/Users/abhij/PycharmProjects/PythonPractice01/playwright_prac/playwright_prac.html")
    print(page.title())

    # CSS Selector
    page.locator("input[name='gender']").nth(0).click()

    time.sleep(4)
    browser.close()