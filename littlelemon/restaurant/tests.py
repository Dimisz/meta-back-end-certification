from django.test import TestCase
from  django.urls import reverse 

# Create your tests here.
class HomePageTest(TestCase):
  def test_url_exists_at_correct_location(self):
    response = self.client.get("/")
    self.assertEqual(response.status_code, 200)
  
  def test_url_available_by_name(self):
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
  
  def test_correct_template_used(self):
    response = self.client.get(reverse("home"))
    self.assertTemplateUsed(response, "index.html")
    self.assertContains(response, "The Little Lemon Restaurant is open 7 days a week, except for public holidays.")
  
