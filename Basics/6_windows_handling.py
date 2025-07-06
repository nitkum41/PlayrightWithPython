from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://demo.automationtesting.in/Windows.html")
    page.wait_for_selector("//button[contains(text(),'    click   ')]").click()

    page.wait_for_timeout(2000)

    #total pages

    total_pages = context.pages
    print("total pages",len(total_pages))

    for p in total_pages:
        print("page",p)

    new_page = total_pages[1]

    print("parent title", page.title())

    #switch to new page/window
    new_page.bring_to_front()
    new_page.wait_for_timeout(2000)

    print("child page",new_page.title())
    # new_page.close()
    
    ##go back to parent window/page
    page.bring_to_front()

    page.wait_for_timeout(2000)

    browser.close()
