from django.test import TestCase


from newsletter.models import Header, Footer, Content


class HeaderTests(TestCase):
    def setUp(self):
        Header.objects.create(email_title="an email from me", email_from='example@gmail.com')

    def test_email_title(self):
        email = Header.objects.get(id=1)
        field_label = email._meta.get_field('email_title').verbose_name
        self.assertEquals(field_label, 'email title')

    def test_email_from(self):
        email = Header.objects.get(id=1)
        field_label = email._meta.get_field('email_from').verbose_name
        self.assertEquals(field_label, 'email from')

    def test_string_representation(self):
        title = Header(email_title="Hello there")
        self.assertEquals(str(title), title.email_title)


class ContentTests(TestCase):
    def setUp(self):
        Content.objects.create(text='hello there!')

    def test_text(self):
        text = Content(text="hello there")
        self.assertEquals(str(text), text.text)


class FooterTests(TestCase):
    def setUp(self):
        Footer.objects.create(link='www.example.com')

    def test_link(self):
        link = Footer.objects.get(id=1)
        expected_link = f'{link.link}'
        self.assertEquals(expected_link, 'www.example.com')
