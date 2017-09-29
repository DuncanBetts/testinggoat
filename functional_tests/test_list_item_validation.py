# pylint: disable=C0103
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from .list_page import ListPage


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        list_page = ListPage(self)
        item_input_box = list_page.get_item_input_box()
        item_input_box.send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load the
        # list page
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # She starts typing some text for the new item and the error disappears
        item_input_box.send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        # And she can submit it successfully
        item_input_box.send_keys(Keys.ENTER)
        item_num = 1
        list_page.wait_for_row_in_list_table('Buy milk', item_num)

        # Perversely, she now decides to submit a second blank list item
        list_page.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        list_page.wait_for_row_in_list_table('Buy milk', item_num)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # And she can correct it by filling some text in
        list_page.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))
        list_page.get_item_input_box().send_keys(Keys.ENTER)
        list_page.wait_for_row_in_list_table('Buy milk', item_num)
        item_num += 1
        list_page.wait_for_row_in_list_table('Make tea', item_num)

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Buy wellies')

        # She accidentally tries to enter a duplicate item
        item_input_box = list_page.get_item_input_box()
        item_input_box.send_keys('Buy wellies')
        item_input_box.send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a list and causes a validation error
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Banter too thick')
        item_input_box = list_page.get_item_input_box()
        item_input_box.send_keys('Banter too thick')
        item_input_box.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # She starts typing in the input box to clear the error
        list_page.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message disappears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))

    def test_error_messages_are_cleared_on_input_focus(self):
        # Edith starts a list and causes a validation error
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Banter too thick')
        item_input_box = list_page.get_item_input_box()
        item_input_box.send_keys('Banter too thick')
        item_input_box.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # She selects the input box to clear the error
        list_page.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message disappears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
