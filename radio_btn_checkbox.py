from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    page = browser.new_page()

    # page.goto("https://demo.automationtesting.in/")

    page.goto("https://demo.automationtesting.in/Register.html")

    # radio_button
    radio_btn = page.query_selector('//input[@value="Male"]')
    radio_btn.click()

    page.wait_for_timeout(2000)

    radio_btn_2= page.query_selector('//input[@value="FeMale"]')
    radio_btn_2.check()

    if radio_btn.is_checked() or radio_btn_2.is_checked():
        print("pass")

    #checkbox
    checkbox_1 = page.query_selector('//input[@value="Cricket"]')
    checkbox_1.click()

    page.wait_for_timeout(2000)

    checkbox_2 = page.query_selector('//input[@value="Movies"]')
    checkbox_2.click()

    if checkbox_1.is_checked() and checkbox_2.is_checked():
        print("pass")


