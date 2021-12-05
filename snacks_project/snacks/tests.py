# from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTests(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('aboutus')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_wrong_url_returns_404(self):
         response = self.client.get('templates/home1.html')
         self.assertEqual(response.status_code, 404)
  
        
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "_base.html")
        

    def test_aboutus_page_template(self):
        url = reverse('aboutus')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "aboutus.html")
        self.assertTemplateUsed(response, "_base.html")

