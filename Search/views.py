from django.shortcuts import render, redirect
from Products.models import Product, Find_a_Part
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def SearchBar(request):
    if request.method=="POST":
            product_OEM = request.POST.get('searched')
            filter_oem_middleware = Product.objects.filter(product_OEM__contains = product_OEM)
            page = request.GET.get('page', 1)
            paginator = Paginator(filter_oem_middleware, 12)
            try:
                filter_oem = paginator.page(page)
            except PageNotAnInteger:
                filter_oem = paginator.page(1)
            except EmptyPage:
                filter_oem = paginator.page(paginator.num_pages)
            return render(request, 'search/OEM.html', {'product':filter_oem, 'term':request.POST.get('searched')})

def Filters(request):
    if request.method == 'POST':
        if request.POST.get('subcategory') and request.POST.get("brand"):
            filters_category = Find_a_Part.objects.filter(vehicle_type = request.POST.get('Vtype'),
                                                    make = request.POST.get('Make'), 
                                                    model = request.POST.get('Model'), 
                                                    year__contains = request.POST.get('Year'),
                                                    category = request.POST.get("category"),
                                                    sub_category = request.POST.get('subcategory'),
                                                    brand = request.POST.get("brand"))
        elif request.POST.get('subcategory'):
            filters_category = Find_a_Part.objects.filter(vehicle_type = request.POST.get('Vtype'),
                                                    make = request.POST.get('Make'), 
                                                    model = request.POST.get('Model'), 
                                                    year__contains = request.POST.get('Year'),
                                                    category = request.POST.get("category"),
                                                    sub_category = request.POST.get('subcategory'))
        else:
            filters_category = Find_a_Part.objects.filter(vehicle_type = request.POST.get('Vtype'),
                                                    make = request.POST.get('Make'), 
                                                    model = request.POST.get('Model'), 
                                                    year__contains = request.POST.get('Year'),
                                                    category = request.POST.get("category"))
        product_filter =  Product.objects.filter(product_find_part = filters_category.values('id')[0]['id'])
        return render(request, 'search/filters.html', {'product':product_filter})
    return render(request, 'search/filters.html')

