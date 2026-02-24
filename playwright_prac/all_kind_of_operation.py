# from playwright.sync_api import sync_playwright, expect
#
# from playwright_prac.web_table import browser
# from selenium_prac.full_automation import frame
#
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('url')
#
#     # locator
#
#
#     # click
#     # left click
#     page.locator().click()
#
#     # double click
#     page.locator().dblclick()
#
#     # right click
#     page.locator().click(button='right')
#
#     # middle click
#     page.locator().click(button='middle')
#
#     # click with modifiers(CTRL/SHIFT)
#     page.locator().click(modifiers=["Control"])
#     page.locator().click(modifiers=['Shift'])
#
#     # force click(Ignore Visibility Issue)
#     page.locator().click(force=True)
#
#     # MOUSE ACTION (Full control over the mouse)
#     # move mouse
#     page.mouse.move(x=0,y=100)
#
#     # mouse down
#     page.mouse.down()
#
#     # mouse up
#     page.mouse.up()
#
#     # drag and drop
#     page.drag_and_drop("#source","#target")
#
#     # hover
#     page.locator("target").hover()
#
#     # scroll using mouse wheel
#     # scroll down
#     page.mouse.wheel(0,500)
#
#     # scroll down and up
#     page.locator().scroll_into_view_if_needed()
#
#     # scroll with the help of java script
#     page.evaluate("js scripts")
#
#
#     # keyboard interaction
#     # type text
#     page.locator().fill()
#
#     # type slowly in test box
#     page.locator().type("name", delay=100)
#
#     # clear text
#     page.locator().clear()
#
#
#     # press key
#     page.keyboard.press("Enter")
#     page.keyboard.press("Tab")
#     page.keyboard.press("Control+A")
#
#     # cleck box
#     # cleck
#     page.locator().check()
#
#     # uncheck
#     page.locator().uncheck()
#
#     # radio
#     page.locator().check()
#
#     # drop down interaction
#     # Select by Value
#     page.locator().select_option("Value")
#
#     # select by lebel
#     page.locator().select_option(label='lable name')
#
#     # select by index
#     page.locator().select_option(index=3)
#
#     # upload a file
#     page.locator().set_input_files("file name")
#
#     # alert & popup
#     page.once("dialog",lambda dialog:dialog.accept())
#     page.once("dialog",lambda dialog:dialog.dismiss())
#
#     def dialog_handle(dialog)
#         dialog = dialog.accept
#         page.locator("")
#     page.once("dialog", dialog_handle())
#
#
#     # frame handle
#     frame = page.frame(name='ABhi')
#     frame.locator().click()
#     # or
#     page.frame_locator().locator().click()
#
#     # wait command
#     page.wait_for_selector()
#     page.wait_for_timeout(5000)
#     page.wait_for_load_state("Locater")
#
#     #assertion in pw(Very IMP)
#     expect(page).not_to_have_title("Dashboard") #title assertion
#     expect(page.locator()).to_have_text("OK") #text ass
#     expect(page.locator()).to_be_visible()
#     expect(page.locator()).to_be_checked()
#     expect(page.locator())