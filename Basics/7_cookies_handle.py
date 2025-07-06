from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")

    #read cookies
    my_cookies = page.context.cookies()

    print("cookie details :",my_cookies[0])

    for k,v in my_cookies[0].items():
        print(k,v)
    #clear cookies
    page.context.clear_cookies()

    #new cokies add
    new_cookies = {
    'name': 'Nitesh', 'value': 'RESPONSIVE', 'domain': 'www.test.in', 'path': '/', 'expires': 1752390463.268385, 'httpOnly': False, 'secure': True, 'sameSite': 'Lax'
    }

    page.context.add_cookies([new_cookies])


    #taking screenshots

    page.screenshot(path='test.png', full_page=True)