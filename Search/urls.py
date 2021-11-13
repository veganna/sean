from django.urls import path, include
from .views import *

app_name = 'Search'

urlpatterns = [
    path('searchbar/', SearchBar, name='searchbar'),
    path('filters/', Filters, name='filters'),
]
