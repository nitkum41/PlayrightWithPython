from playwright.sync_api import sync_playwright


def handle_download(download):
    file_location = './Downloads/sampleFile.pdf'
    download.save_as(file_location)



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #by default is headless
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://demo.automationtesting.in/FileUpload.html")

    #upload a file

    file_upload = './test.txt'

    upload_location=page.query_selector("//input[@id='input-4']")

    #upload_file

    upload_location.set_input_files(file_upload)

    page.wait_for_timeout(3000)

    #download_file

    try:


        page.goto("https://demo.automationtesting.in/FileDownload.html")

        page.on('download',handle_download)
        download_link = page.query_selector("//a[text()='Download' and @type='button']")
        download_link.click()
        page.wait_for_timeout(3000)
    except Exception as e:
        print("Error :" , e)





