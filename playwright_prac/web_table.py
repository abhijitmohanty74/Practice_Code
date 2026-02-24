from turtledemo.sorting_animate import instructions1

from playwright.sync_api import sync_playwright
import time

url = "https://rahulshettyacademy.com/AutomationPractice/"
# test data
expected_instructor = "Rahul Shetty"
expected_sum = None
actual_instructor = []
actual_price = []
with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    print(page.title())
    time.sleep(2)


    table  = page.locator("(//table[@id='product'])[1]")
    rows = table.locator('tr')
    row_count = rows.count()


    for i in range(1,row_count):
        row = rows.nth(i)
        # print(row.text_content())
        cols = row.locator('td')
        # print(cols.count())

        # skip if not a proper data row
        if cols.count()<3:
            continue
        # actual_instructor  =
        instructor = cols.nth(0).inner_text().strip()
        price = cols.nth(2).inner_text().strip()
        print(instructor,price)

    for j in range(1,12):
        if expected_instructor == instructor:
            print(j,"pass")
        else:
            print(j,'fail')
    # for j in actual_instructor:
    #     if expected_instructor == j:
    time.sleep(2)
    browser.close()