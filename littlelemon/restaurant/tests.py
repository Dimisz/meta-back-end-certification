from django.test import TestCase
from  django.urls import reverse 

from .models import Menu, Booking

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
    self.assertEqual(self.menu.get_absolute_url(), "/menu/1")

  def test_url_exists_at_correct_location_listview(self):
    response = self.client.get("/menu/")
    self.assertEqual(response.status_code, 200)

  def test_url_exists_at_correct_location_detailview(self):
    response = self.client.get("/menu/1")
    self.assertEqual(response.status_code, 200)
  
  def test_menu_listview(self):
    response = self.client.get(reverse("menu"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "menu.html")
    self.assertContains(response, "<h1>Menu</h1>")

  def test_menu_detailview(self):
    response = self.client.get(reverse("menu_item", kwargs={"pk": self.menu.pk}))
    no_response = self.client.get("/menu/1000")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertTemplateUsed(response, "menu_item.html")
    self.assertContains(response, "<h1>Menu item</h1>")

class BookingTests(TestCase):
    @classmethod
    def setUpTestData(cls):
      cls.booking = Booking.objects.create(
        first_name = "John",
        last_name = "Doe", 
        guest_number = 5,
        comment = "Test comment"
      )
    
    def test_booking_model(self):
      self.assertEqual(self.booking.first_name, "John")
      self.assertEqual(self.booking.last_name, "Doe")
      self.assertEqual(self.booking.guest_number, 5)
      self.assertEqual(self.booking.comment, "Test comment")

    def test_url_exists_at_correct_location(self):
      response = self.client.get("/book/")
      self.assertEqual(response.status_code, 200)
    
    def test_booking_formview(self):
      response = self.client.post(
        reverse("book"),
        {
          "first_name": "Mary",
          "last_name": "Smith",
          "guest_number": "12",
          "comment": "Birthday party"
        },
      )
      self.assertEqual(response.status_code, 302)
      self.assertEqual(Booking.objects.last().first_name, "Mary")
      self.assertEqual(Booking.objects.last().last_name, "Smith")
      self.assertEqual(Booking.objects.last().guest_number, 12)
      self.assertEqual(Booking.objects.last().comment, "Birthday party")
    


  
