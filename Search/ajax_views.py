from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from Products.models import Find_a_Part


def GetVehicleType(request):
    data=request.GET.get('Data-Vtype')
    vehicle_type_queryset_middleware = Find_a_Part.objects.values('vehicle_type')
    vehicle_type_queryset = []
    for i in vehicle_type_queryset_middleware:
        if i not in vehicle_type_queryset:
            vehicle_type_queryset.append(i)
    return JsonResponse(vehicle_type_queryset, safe=False)

def GetMake(request):
    data=request.GET.get('Data-Vtype')
    make_queryset_middleware = Find_a_Part.objects.filter(vehicle_type = data).values('make')
    make_queryset = []
    for i in make_queryset_middleware:
        if i not in make_queryset:
            make_queryset.append(i)
    return JsonResponse(make_queryset, safe=False)

def GetModel(request):
    data_Vtype = request.GET.get('Data-Vtype')
    data_Make = request.GET.get('Data-Make')
    model_queryset_middleware = Find_a_Part.objects.filter(vehicle_type = data_Vtype, make = data_Make).values('model')
    model_queryset = []
    for i in model_queryset_middleware:
        if i not in model_queryset:
            model_queryset.append(i)
    return JsonResponse(model_queryset, safe=False)

def GetYear(request):
    data_Vtype = request.GET.get('Data-Vtype')
    data_Make = request.GET.get('Data-Make')
    data_Model = request.GET.get('Data-Model')
    years = Find_a_Part.objects.filter(vehicle_type = data_Vtype, make = data_Make, model = data_Model).values('year')
    newlist = []
    for each in years:
    	newv = each.get("year")
    	for each in newv.split(' '):
    		if each not in newlist:
    			newlist.append(each)
    finallist = []
    for each in newlist:
    	finallist.append({"year" : each})
    return JsonResponse(finallist, safe=False)

def GetCategory(request):
    data_Vtype = request.GET.get('Data-Vtype')
    data_Make = request.GET.get('Data-Make')
    data_Model = request.GET.get('Data-Model')
    data_Year = request.GET.get('Data-Year')
    category_queryset_middleware = Find_a_Part.objects.filter(vehicle_type = data_Vtype, make = data_Make,model = data_Model, year__contains = data_Year).values('category')
    category_queryset = []
    for i in category_queryset_middleware:
        if i not in category_queryset:
            category_queryset.append(i)
    return JsonResponse(category_queryset, safe=False)

def GetSubCategory(request):
    data_Vtype = request.GET.get('Data-Vtype')
    data_Make = request.GET.get('Data-Make')
    data_Model = request.GET.get('Data-Model')
    data_Year = request.GET.get('Data-Year')
    data_Category = request.GET.get('Data-Category')
    subcategory_queryset_middleware = Find_a_Part.objects.filter(vehicle_type = data_Vtype, make = data_Make,model = data_Model, year__contains = data_Year, category=data_Category).values('sub_category')
    subcategory_queryset = []
    for i in subcategory_queryset_middleware:
        if i not in subcategory_queryset:
            subcategory_queryset.append(i)
    return JsonResponse(subcategory_queryset, safe=False)

def GetBrand(request):
    data_Vtype = request.GET.get('Data-Vtype')
    data_Make = request.GET.get('Data-Make')
    data_Model = request.GET.get('Data-Model')
    data_Year = request.GET.get('Data-Year')
    data_Category = request.GET.get('Data-Category')
    data_Subcategory = request.GET.get('Data-Subcategory')
    brand_queryset_middleware = Find_a_Part.objects.filter(vehicle_type = data_Vtype, make = data_Make,model = data_Model, year__contains = data_Year, category = data_Category, sub_category=data_Subcategory).values('brand')
    brand_queryset = []
    for i in brand_queryset_middleware:
        if i not in brand_queryset:
            brand_queryset.append(i)
    return JsonResponse(brand_queryset, safe=False) 



