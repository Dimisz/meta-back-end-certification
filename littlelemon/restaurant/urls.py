from django.urls import path

from .views import HomeView, AboutView, BookingView

urlpatterns = [
  path("", HomeView.as_view(), name="home"),
  path("about/", AboutView.as_view(), name="about"),
  path("book/", BookingView.as_view(), name="book"),
  path("menu/", BookingView.as_view(), name="menu"),
]