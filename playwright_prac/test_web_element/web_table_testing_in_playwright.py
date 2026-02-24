import json
from playwright.sync_api import sync_playwright

from playwright_prac.test_web_element.json_handel_in_python import return_test_data
from playwright_prac.web_table import actual_instructor

url = "https://rahulshettyacademy.com/AutomationPractice/"
expected_web_instructor = []
expected_web_courses = []
expected_web_price = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    table = page.locator("(//table[@id='product'])[1]")
    rows = table.locator('tr')
    row_count = rows.count()

    web_table_data = {}

    for i in range(1, row_count):
        cols = rows.nth(i).locator("td")
        if cols.count() < 3:
            continue

        expected_web_instructor.append(cols.nth(0).inner_text().strip())
        expected_web_courses.append(cols.nth(1).inner_text().strip())
        expected_web_price.append(cols.nth(2).inner_text().strip())
    print(expected_web_instructor,expected_web_courses, expected_web_price)

    test_data = return_test_data()
    for idx,value in enumerate(test_data):
        if idx == 0:
            for j in expected_web_instructor:
                assert j == value,f'{j} == {value} both are not match'

    actual_course = []
    for i in test_data[1]:
        actual_course.append(i['course_name'])
    assert  len(expected_web_courses) == len(actual_course)
    
    for i in range(len(expected_web_courses)):
        assert  expected_web_courses[i] == actual_course, f'{expected_web_courses}'
    # Read JSON file
    # with open("test_json_data.json") as file:
    #     data = json.load(file)
    #
    # # Validate and Print Each Row
    # for index, course in enumerate(data["courses"], start=1):
    #
    #     print(f"\nValidating Row {index}")
    #     print("Course Name:", course.get("course_name"))
    #     print("Price:", course.get("price"))
    #
    #     if course.get("course_name") and \
    #        course.get("price") is not None and \
    #        isinstance(course.get("price"), (int, float)) and \
    #        course.get("price") >= 0:
    #
    #         print(f"Row {index} Passed")
    #     else:
    #         print(f"Row {index} Failed")

    browser.close()