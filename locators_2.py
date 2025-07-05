from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    page = browser.new_page()
    # page.goto("https://demo.automationtesting.in/")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("url is : ", page.url)

    print("title is :", page.title())

    #text()

    page.wait_for_selector('//p[contains(@text(),"Forgot your")]').click()

    #contains
    # //label[contains(text(),"Username")]
    # //input[contains(@placeholder,"User")]

    #starts-with(@id,'val')
    #ends-with(@id,'val')

    #family
    # parent //tag[@id="val"]/parent::input[]
    # child //tag[@id="val"]/child::input[]
    # ancestor
    # siblings - //tag[@id='val']//following-sibling:: td[2]



    # page.wait_for_selector('//p[text()="Forgot your password? "]').click()

    #xpath //
    # username = page.wait_for_selector('//input[@name="username"]')
    # username.type("Admin")
    # password = page.wait_for_selector('//input[@name="password"]')
    # password.type("admin123")
    #
    # loginButton = page.wait_for_selector('//button[@type="submit"]')
    # loginButton.click()

    page.wait_for_timeout(3000)