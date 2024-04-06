from django.urls import path

from .views import scraping

urlpatterns = [
    path("", scraping, name="scraping"),
]
