from django.urls import path, include
from .views import *


app_name = 'Product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_listview'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detailview'),
    path('ajax/', include('Products.ajaxurls')),
    path('land/<str:vland>', ProductListByLand, name="land"),
]
