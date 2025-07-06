from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    page = browser.new_page()

    # page.goto("https://demo.automationtesting.in/")

    page.goto("https://demo.automationtesting.in/Register.html")

    #Select
    # dropdown = page.query_selector('//select[@id="Skills"]')
    #1
    page.select_option('//select[@id="Skills"]',label='Android')

    page.wait_for_timeout(3000)


