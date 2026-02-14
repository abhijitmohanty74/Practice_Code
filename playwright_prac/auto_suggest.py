from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")
    #print the title in playwright
    print(page.title())

    page.fill("#autocomplete","us")
    elements = page.locator("li[class='ui-menu-item'] div")
    time.sleep(3)
    count = elements.count()
    print(count)

    # for i in range(count):


    browser.close()