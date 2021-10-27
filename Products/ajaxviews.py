from django.shortcuts import render
from .models import Category, Find_a_Part, Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def GetVehicleLand(request):
    data=request.GET.get('Data-Vland')
    vehicle_land_queryset_middleware = Category.objects.values('vehicle_land')
    vehicle_land_queryset = []
    for i in vehicle_land_queryset_middleware:
        if i not in vehicle_land_queryset:
            vehicle_land_queryset.append(i)
    return JsonResponse(vehicle_land_queryset, safe=False)

def GetVehicleType(request):
    data=request.GET.get('Data-Vland')
    vehicle_type_queryset_middleware = Category.objects.filter(vehicle_land = data).values('vehicle_type')
    vehicle_type_queryset = []
    for i in vehicle_type_queryset_middleware:
        if i not in vehicle_type_queryset:
            vehicle_type_queryset.append(i)
    return JsonResponse(vehicle_type_queryset, safe=False)

def GetCategory(request):
    data_Vland=request.GET.get('Data-Vland')
    data_Vtype=request.GET.get('Data-Vtype')
    category_queryset_middleware = Category.objects.filter(vehicle_land = data_Vland, vehicle_type = data_Vtype,).values('category')
    category_queryset = []
    for i in category_queryset_middleware:
        if i not in category_queryset:
            category_queryset.append(i)
    return JsonResponse(category_queryset, safe=False)

def GetSubcategory(request):
    data_Vland=request.GET.get('Data-Vland')
    data_Vtype=request.GET.get('Data-Vtype')
    data_Category=request.GET.get('Data-Category')
    subcategory_queryset_middleware = Category.objects.filter(vehicle_land = data_Vland, vehicle_type = data_Vtype, category = data_Category).values('sub_category')
    subcategory_queryset = []
    for i in subcategory_queryset_middleware:
        if i not in subcategory_queryset:
            subcategory_queryset.append(i)
    return JsonResponse(subcategory_queryset, safe=False)


def Submit(request):
    if request.method == "POST":
        filters_category = Category.objects.filter(vehicle_land = request.POST.get('Vland'),
                                                    vehicle_type = request.POST.get('Vtype'), 
                                                    category = request.POST.get('Category'), 
                                                    sub_category = request.POST.get('Subcategory'))
        product_filter =  Product.objects.filter(product_category = filters_category.values('id')[0]['id'])
        return render(request, 'Products/product_search_list.html', {'product':product_filter})

def ProductIdentifier(request):
    data_identify=request.GET.get('Data-Identify')
    identify_queryset_product = Product.objects.filter(product_SKU=data_identify).values('product_find_part')
    identify_queryset = []
    for e in identify_queryset_product:
        identify_queryset_middleware = Find_a_Part.objects.filter(id=e['product_find_part']).values('vehicle_type', 'make', 'model', 'year')
        for i in identify_queryset_middleware:
            identify_queryset.append(i)
    return JsonResponse(identify_queryset, safe=False)
