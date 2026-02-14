from playwright.sync_api import sync_playwright
import time


with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(r"C:/Users/abhij/PycharmProjects/PythonPractice01/playwright_prac/playwright_prac.html")
    print(page.title())

    fname = page.locator("#fname")
    fname.fill("Abhijit")

    page.fill("#lname", "Mohanty")

    email = page.locator("#email")
    email.fill("abhi@.com")

    page.fill("#mobile", "1234567890")

    time.sleep(4)
    browser.close()