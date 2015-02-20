from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import homepage


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        go = resolve('/')

        self.assertEqual(go.func, homepage)


class TestPosting(TestCase):
    def test_if_post_request_works(self):
        response = self.client.post('/', data={'url': 'http://en.wikipedia.org/wiki/Thomas_Mensah'})

        # print(response.context)
        self.assertContains(response.context, 'extract')
