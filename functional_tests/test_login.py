# pylint: disable=C0103
import re

from .login_page import LoginPage
from .base import FunctionalTest

SUBJECT = 'Your login link for SuperLists'


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        if self.staging_server:
            test_email = 'rootduncan@outlook.com'
        else:
            test_email = 'edith@example.com'

        self.browser.get(self.live_server_url)
        login_page = LoginPage(self).login(test_email)

        # A message appears telling her an email has been sent
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            login_page.get_login_message()
        ))

        # She checks her email and finds a message
        email_body = self.wait_for_email(test_email, SUBJECT)

        # It has a url link in it
        self.assertIn('Use this link to log in', email_body)
        url_search = re.search(r'http://.+/.+$', email_body)
        if not url_search:
            self.fail('Could not find url in email body:\n{}'
                      .format(email_body))
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # She clicks it
        self.browser.get(url)

        # She is logged in!
        login_page.wait_to_be_logged_in(email=test_email)

        # Now she logs out
        login_page.logout()

        # She is logged out
        login_page.wait_to_be_logged_out(email=test_email)
