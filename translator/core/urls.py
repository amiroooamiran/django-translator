from django.urls import path
from .views import *

urlpatterns = [
    path('', scraping, name="scraping" )
]
