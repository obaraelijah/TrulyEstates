from django.test import TestCase, Client
from django.urls import reverse
from .models import Listing

class TestViews(TestCase):
    def setUp(self):
      self.client = Client()
      self.index_url =  reverse('listings:index')
      self.search_url = reverse('listings:search')
      self.listing = Listing.objects.create(title='Test Listing', is_published=True)
      self.listing_url = reverse('listings:listing', args=[self.listing.pk])
    
    
    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/index.html')
        
    def test_listing_view(self):
        response = self.client.get(self.listing_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing.html')

    def test_search_view(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/search.html')
        
    def test_search_view_with_parameters(self):
        response = self.client.get(self.search_url, {'state': 'NB', 'bedrooms': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/search.html')
        self.assertContains(response, self.listing.title)