from django.test import TestCase, Client
from django.urls import reverse
from listings.models import Listing
from realtors.models import Realtor

class PagesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('pages:index')
        self.about_url = reverse('pages:about')
        self.listing = Listing.objects.create(
            title='Test Listing',
            address='123 Test Street',
            price=100000,
            photo_main='test.jpg',
            is_published=True
        )
        self.realtor = Realtor.objects.create(
            name='Test Realtor',
            email='test@example.com',
            phone='555-555-5555',
            is_mvp=True,
            hire_date='2022-01-01'
        )

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertContains(response, self.listing.title)
        self.assertContains(response, self.listing.address)
        self.assertContains(response, self.listing.price)
        self.assertContains(response, self.listing.photo_main)
        self.assertContains(response, 'Search Properties')
        self.assertContains(response, 'Popular Cities')
        self.assertContains(response, 'Price')
        self.assertContains(response, 'Bedrooms')
        self.assertContains(response, 'States')

    def test_about_view(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
        self.assertContains(response, self.realtor.name)
        self.assertContains(response, self.realtor.email)
        self.assertContains(response, self.realtor.phone)
        self.assertContains(response, 'Our Team')
        self.assertContains(response, 'Meet Our Realtors')
        self.assertContains(response, 'MVP Realtor')
