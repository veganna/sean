"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login.urls', namespace='Account')),
    path('', include('StaticPages.urls', namespace='Pages')),
    path('product/', include('Products.urls', namespace='Product')),
    path('search/', include('Search.urls', namespace='Search')),
    path('search/ajax/', include('Search.ajax_urls', namespace='Ajax')),
    path("cart/", include("Cart.urls", namespace="Cart")),
    path("staff/", include("Staff.urls", namespace="Staff")),
    path("order/", include("Orders.urls", namespace="Orders")),
    path("payment/", include("Payments.urls", namespace="Payments")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

