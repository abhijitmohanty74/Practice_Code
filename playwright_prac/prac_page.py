from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto(r"C:\Users\abhij\PycharmProjects\PythonPractice01\playwright_prac\playwright_prac.html")
    #print the title in playwright
    print(page.title())

    #form of input box
    first_name = page.locator("#fname")
    first_name.fill("satya")

    page.fill("#lname",'Prakash')
    page.fill("#email","satya@test.com")

    #radio button
    page.locator("input[name='gender']").nth(1).click()
    # page.locator("//input[@name='gender'][2]").click()  # xpath

    page.fill("#mobile","9876543210")

    page.fill("input[type='date']","1977-03-01")

    page.set_input_files("input[type='file']",r"C:\Users\abhij\PycharmProjects\PythonPractice01\playwright_prac\playwright_prac.html")

    page.select_option("select", value="South Africa")

    # page.fill("#countrySearch")

    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")

    time.sleep(5)

    browser.close()