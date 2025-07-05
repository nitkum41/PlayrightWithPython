from playwright.sync_api import sync_playwright
text_alert=[]



def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()



def handle_dialog_textbox(dialog):
    message = dialog.message
    text_alert.append(message)
    type = dialog.type
    text_alert.append(type)

    dialog.accept("Nitesh Kumar")



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    page = browser.new_page()

    # page.goto("https://demo.automationtesting.in/")

    page.goto("https://demo.automationtesting.in/Alerts.html")

    #by default clicks on OK
    # page.wait_for_selector("//button[@onclick='alertbox()']")

    # page.query_selector("//a[@href='#CancelTab']").click()
    #
    # page.wait_for_timeout(2000)
    #
    # ##control alert----------->>>>>>>>>>>>>Note
    #
    # page.on("dialog",handle_dialog)
    #
    # # page.on("dialog", lambda dialog: dialog.dismiss())
    #
    # page.wait_for_selector("//button[@onclick='confirmbox()']").click()
    #
    # print(text_alert)


    ##assign

    page.query_selector("//a[@href='#Textbox']").click()

    page.wait_for_timeout(2000)

    ##control alert----------->>>>>>>>>>>>>Note

    page.on("dialog", handle_dialog_textbox)

    # page.on("dialog", lambda dialog: dialog.dismiss())

    page.wait_for_selector("//button[@onclick='promptbox()']").click()

    print(text_alert)



    page.wait_for_timeout(2000)