from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #by default is headless
    page = browser.new_page()
    page.goto("https://www.google.co.in")
    print("url is : ",page.url)
    page.wait_for_timeout(3000)
    print("title is :",page.title())
    browser.close()
