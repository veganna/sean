from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from Cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class ProductListView(ListView):
    paginate_by = 12
    def get_queryset(self):
        queryset = Product.objects.filter(is_active = True)
        return queryset

class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_active=True)
    extra_context = {"form": CartAddProductForm()}

def ProductListByLand(request, vland):
    queryset_middleware = Product.objects.filter(product_category__vehicle_land__contains = vland)
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset_middleware, 12)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return render(request, 'search/OEM.html', {'product':queryset, 'term': vland})
