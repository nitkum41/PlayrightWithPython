from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://demo.automationtesting.in/Selectable.html")

    elements = page.query_selector_all("//ul[@class='deaultFunc']/li")

    print("length :",len(elements))
    print("data :",elements)

    for item in elements:
        # print(item.text_content())
        # print(item.inner_text())
        print(item.get_attribute('class'))
    page.wait_for_timeout(2000)


