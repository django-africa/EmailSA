from django.test import TestCase, Client


class HeaderViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_api_header(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_get_api_content(self):
        response = self.client.get('/content/')
        self.assertEquals(response.status_code, 200)

    def test_get_api_footer(self):
        response = self.client.get('/footer/')
        self.assertEquals(response.status_code, 200)


