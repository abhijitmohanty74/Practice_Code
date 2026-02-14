from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")
    #print the title in playwright
    print(page.title())

    # page.select_option("select" , "Option3")
    page.select_option("select" , index=2)

    time.sleep(3)

    browser.close()