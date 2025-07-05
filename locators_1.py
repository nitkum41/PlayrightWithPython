from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    page = browser.new_page()
    # page.goto("https://demo.automationtesting.in/")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("url is : ", page.url)

    print("title is :", page.title())

    # #css selector ID #
    # emailTxtBox = page.wait_for_selector('#email')
    # emailTxtBox.type("abc@gmail.com")
    #
    # loginButton = page.wait_for_selector('#enterimg')
    # loginButton.click()



    # CLASS .
    # Attribute
    username = page.wait_for_selector('input[name="username"]')
    username.type("Admin")
    password = page.wait_for_selector('input[name="password"]')
    password.type("admin123")

    loginButton = page.wait_for_selector('button[type="submit"]')
    loginButton.click()

    page.wait_for_timeout(3000)



    browser.close()
