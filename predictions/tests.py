from rest_framework.test import APITestCase
from django.urls import reverse

class RegionAPITestCase(APITestCase):
    def test_get_regions(self):
        url = reverse('region-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)