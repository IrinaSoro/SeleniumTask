import allure
from pages.upload_file_page import UploadFilePage

@allure.suite('File upload')
class TestUploadFilePage:

    @allure.title('Check file upload')
    def test_upload_file(self, driver):
        upload_file_page = UploadFilePage(driver, "https://webdriveruniversity.com/File-Upload/index.html")
        upload_file_page.open()
        is_alert_present = upload_file_page.upload_file()
        print(is_alert_present)