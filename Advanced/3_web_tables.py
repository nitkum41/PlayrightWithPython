from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")

    table = page.wait_for_selector("//table[@id='customers']")
    rows = table.query_selector_all('tr')
    print("no of rows",len(rows))

    cols = table.query_selector_all('td')
    print("no of columns", len(cols))

    page.wait_for_timeout(2000)

    for row in rows:
        cols_in_row = row.query_selector_all('td')
        for col in cols_in_row:
            print(col.inner_text())


