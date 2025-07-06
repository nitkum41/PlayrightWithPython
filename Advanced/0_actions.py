from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://demo.automationtesting.in/Selectable.html")

    #mouse Actions
    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").hover()
    page.wait_for_timeout(2000)

    #single click
    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").click()

    #double click
    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").dblclick()

    #rightclick

    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").click(button="right")

    #shift+click

    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").click(modifiers=["Shift"])

    page.wait_for_timeout(2000)

    ##keyboard Actions

    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").press("A")

    page.wait_for_selector("//a[contains(text(),'SwitchTo')]").press("$")

    page.wait_for_timeout(2000)