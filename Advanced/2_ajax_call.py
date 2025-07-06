from playwright.sync_api import sync_playwright


def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        status = response.status
        data = response.text()
        print(f'status is {status} and data is {data}')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php")

    select = page.wait_for_selector("//select[@id='s1']")
    #listener
    page.on('response',lambda response : handle_rejex(response))
    select.select_option('3')

    page.wait_for_timeout(2000)