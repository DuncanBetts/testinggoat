# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
