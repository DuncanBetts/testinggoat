from selenium.webdriver.common.keys import Keys
from .base import wait


class LoginPage(object):

    def __init__(self, test):
        self.test = test

    def get_login_box(self):
        return self.test.browser.find_element_by_name('email')

    def get_login_message(self):
        return self.test.browser.find_element_by_tag_name('body').text

    def login(self, email):
        self.get_login_box().send_keys(email)
        self.get_login_box().send_keys(Keys.ENTER)
        return self

    def get_logout_link(self):
        return self.test.browser.find_element_by_link_text('Log out')

    def logout(self):
        self.get_logout_link().click()

    @wait
    def wait_to_be_logged_in(self, email):
        self.test.browser.find_element_by_link_text('Log out')
        navbar = self.test.browser.find_element_by_css_selector('.navbar')
        self.test.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        self.test.browser.find_element_by_name('email')
        navbar = self.test.browser.find_element_by_css_selector('.navbar')
        self.test.assertNotIn(email, navbar.text)
