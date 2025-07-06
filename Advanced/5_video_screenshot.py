

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    #video directory
    context = browser.new_context(record_video_dir='./Videos')
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(3000)
    username = page.query_selector('input[name="username"]')
    username.fill("Admin")
    password = page.query_selector('input[name="password"]')
    password.fill("admin123")

    #screenshot path
    page.screenshot(path='./Screenshots/loginpage.png')

    loginButton = page.query_selector('button[type="submit"]')
    loginButton.click()

    page.wait_for_timeout(3000)

    # screenshot path
    page.screenshot(path='./Screenshots/homepage.png')

    page.wait_for_timeout(3000)

    context.close()

