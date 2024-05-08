from django.urls import path

from .views import HomeView, AboutView, BookingView, MenuListView

urlpatterns = [
  path("", HomeView.as_view(), name="home"),
  path("about/", AboutView.as_view(), name="about"),
  path("book/", BookingView.as_view(), name="book"),
  path("menu/", MenuListView.as_view(), name="menu"),
]