import allure
from pages.contact_us_page import ContactUsPage

@allure.suite('Contact Us')
class TestContactUsPage:

    URL = "/Contact-Us/contactus.html"

    @allure.title('2.1 - Check placeholders')
    def test_fields_placeholders(self, driver):
        contact_us_page = ContactUsPage(driver, self.URL)
        first_name_placeholder, last_name_placeholder, email_placeholder, comments_placeholder = contact_us_page.verify_placeholders()
        required_fields_message = contact_us_page.verify_required_fields()
        assert 'all fields are required' == required_fields_message[1]
        assert first_name_placeholder == 'First Name', 'First name placeholder is not added'
        assert last_name_placeholder == 'Last Name', 'Last name placeholder is not added'
        assert email_placeholder == 'Email Address', 'Email address placeholder is not added'
        assert comments_placeholder == 'Comments', 'Comments placeholder is not added'

    @allure.title('2.2 - Check invalid email error message')
    def test_invalid_email_address_message(self, driver):
        contact_us_page = ContactUsPage(driver, self.URL)
        error_text = contact_us_page.verify_incorrect_email_address_error()
        assert error_text[1] == 'Invalid email address', 'Incorrect email address error message is not shown'

    @allure.title('2.3 - Check successfully sent comment message')
    def test_sent_comment_message(self, driver):
        contact_us_page = ContactUsPage(driver, self.URL)
        new_url, success_message = contact_us_page.verify_successfully_sent_comment()
        assert new_url == 'https://webdriveruniversity.com/Contact-Us/contact-form-thank-you.html', 'URL has not been updated'
        assert success_message == 'Thank You for your Message!', 'Successful message is not shown'

