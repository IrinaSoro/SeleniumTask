import allure
from pages.upload_file_page import UploadFilePage

@allure.suite('File upload')
class TestUploadFilePage:

    URL = "/File-Upload/index.html"

    @allure.title('9 - Check file upload')
    def test_upload_file(self, driver):
        upload_file_page = UploadFilePage(driver, self.URL)
        is_alert_present = upload_file_page.upload_file()
        assert is_alert_present == True, 'The alert is not shown'