from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import homepage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# import time


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        go = resolve('/')

        self.assertEqual(go.func, homepage)

    def test_GET_of_view(self):
        request = self.client.get('/')

        self.assertEqual(request.status_code, 200)
        self.assertIn('Siya', request.content)
        self.assertTemplateUsed('index.html')

    def test_POST_of_view(self):
        response = self.client.post('/', {'url': 'http://en.wikipedia.org/wiki/Thomas_Mensah'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('extract', response.context)


class TestViaBrowser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver'))
        self.browser.implicitly_wait(3)
        # time.sleep(5)

    def tearDown(self):
        self.browser.quit()

    def test_input(self):
        self.browser.get('http://localhost:8000')

        # Check if input field is required.
        required = self.browser.find_element_by_xpath("//input[@required]")
        # Check if there's a reset button
        reset = self.browser.find_element_by_xpath("//input[@type='reset']")
        # try submitting form
        input_box = self.browser.find_element_by_id('url')
        input_box.send_keys('http://en.wikipedia.org/wiki/Thomas_Mensah')
        input_box.submit()
