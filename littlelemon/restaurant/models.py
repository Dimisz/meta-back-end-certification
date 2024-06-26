from django.db import models
from django.urls import reverse
# Create your models here.
class Booking(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  guest_number = models.IntegerField()
  comment = models.CharField(max_length=1000)

  def __str__(self):
    return self.first_name + " " + self.last_name

class Menu(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(max_length=1000, default=" ")
  price = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("menu_item", kwargs={"pk": self.pk})