from django.test import TestCase
from  django.urls import reverse 

from .models import Menu

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



class MenuTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.menu = Menu.objects.create(
      name="Falafel",
      description="Some description here", 
      price=10
    )
  
  def test_menu_model(self):
    self.assertEqual(self.menu.name, "Falafel")
    self.assertEqual(self.menu.price, 10)
    self.assertEqual(self.menu.description, "Some description here")
    self.assertEqual(str(self.menu), "Falafel")

  def test_url_exists_at_correct_location(self):
    response = self.client.get("/menu/")
    self.assertEqual(response.status_code, 200)
  
  def test_url_available_by_name(self):
    response = self.client.get(reverse("menu"))
    self.assertEqual(response.status_code, 200)
  
  def test_correct_template_used(self):
    response = self.client.get(reverse("menu"))
    self.assertTemplateUsed(response, "menu.html")
    self.assertContains(response, "<h1>Menu</h1>")


  
