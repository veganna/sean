from django.shortcuts import render
import openpyxl
from Products.models import Category, Product, Find_a_Part

# Create your views here.

def get_category(p):
    vehicle_land = p[0]
    vehicle_type = p[1]
    category = p[2]
    sub_category = p[3]
    categorymodel = Category.objects.filter(vehicle_land = vehicle_land, vehicle_type = vehicle_type, category = category, sub_category = sub_category )
    if categorymodel:
        categorymodel = Category.objects.get(vehicle_land = vehicle_land, vehicle_type = vehicle_type, category = category, sub_category = sub_category )
        return categorymodel
    else:
        categorymodel = Category.objects.create(vehicle_land = vehicle_land, vehicle_type = vehicle_type, category = category, sub_category = sub_category)
        categorymodel = Category.objects.get(vehicle_land = vehicle_land, vehicle_type = vehicle_type, category = category, sub_category = sub_category)
        return categorymodel
        

def find_a_part(make, model, year_from, year_to, vehicle_type, productsku, brand,):
    product = Product.objects.get(product_SKU = productsku)
    category1 = product.product_category.category
    subcategory = product.product_category.sub_category

    if year_from:
        if year_to:
            yearfrom = year_from
            yearto = year_to
            all_years = []

            for i in range(yearfrom, yearto+1):
                all_years.append(str(i))
            year = ' '.join([str(elem) for elem in all_years])
        else:
            year = year_from
    else:
        year = None

    category = Find_a_Part.objects.filter(make = make, model = model, year = year, vehicle_type = vehicle_type, category = category1, brand = brand, sub_category=subcategory)
    
    if category:
        category = Find_a_Part.objects.filter(make = make, model = model, year = year, vehicle_type = vehicle_type, category = category1, brand = brand, sub_category=subcategory)
        return category
    else: 
        category = Find_a_Part.objects.create(make = make, model = model, year = year, vehicle_type = vehicle_type, category = category1, brand = brand, sub_category=subcategory)
        category = Find_a_Part.objects.filter(make = make, model = model, year = year, vehicle_type = vehicle_type, category = category1, brand = brand, sub_category=subcategory)
        return category





def ExcelView(request):
    if request.method == 'POST':
        if '.xlsx' in request.FILES['excel'].name:
            excel_file_middleware = request.FILES['excel']
            dir_Excel = 'excel_database/database_products.xlsx'
            
            with open(dir_Excel, 'wb+') as f:
                for chunk in excel_file_middleware.chunks():
                    f.write(chunk)
            

            book = openpyxl.load_workbook(dir_Excel)
	        
            sheet1 = book["Sheet 1"]
            sheet2 = book["Sheet 2"]
            products = []
            v_types = []
            product_add = 0
            Category_add = 0
            
            for row in sheet1.rows:
                products.append(row)
	        
            for p in products:
                if p[11].value == 'Categories':
                    pass
                else:
                    product_add = product_add + 1
                    product_name = p[1].value
                    product_SKU = p[0].value 
                    product_short_description = p[2].value
                    product_description = p[3].value
                    product_stock = p[4].value
                    product_width = p[7].value
                    product_height = p[8].value
                    product_lenght = p[6].value
                    product_weight = p[5].value
                    product_regular_price = p[10].value
                    product_sale_price = p[9].value
                    is_OEM = p[13].value
                    product_OEM = p[14].value
                    
                    if is_OEM:
                        is_OEM = True
                    else:
                        is_OEM = False
                    
                    if product_sale_price:
                        pass
                    else:
                        product_sale_price = product_regular_price
                        
                    product_photo_url = p[12].value
                    product_category_middleware = p[11].value
                    product_list_category_middleware = product_category_middleware.split(', ')
                    product_category = product_list_category_middleware[1].split("> ")
                    category_model = get_category(product_category)
                    if Product.objects.filter(product_SKU = product_SKU):    
                        Product.objects.filter(product_SKU = product_SKU).update(
                            product_name                = product_name,
                            product_SKU                 = product_SKU,
                            product_short_description   = product_short_description,
                            product_description         = product_description,
                            product_stock               = product_stock,
                            product_width               = product_width,
                            product_height              = product_height,
                            product_lenght              = product_lenght,
                            product_weight              = product_weight,
                            product_price               = product_regular_price,
                            product_sale_price          = product_sale_price,
                            product_photo_url           = product_photo_url,
                            product_category            = category_model,
                            product_is_OEM              = is_OEM,
                            product_OEM                 = product_OEM   
                        )
                    else:
                        new_product = Product(
                            product_name                = product_name,
                            product_SKU                 = product_SKU,
                            product_short_description   = product_short_description,
                            product_description         = product_description,
                            product_stock               = product_stock,
                            product_width               = product_width,
                            product_height              = product_height,
                            product_lenght              = product_lenght,
                            product_weight              = product_weight,
                            product_price               = product_regular_price,
                            product_sale_price          = product_sale_price,
                            product_photo_url           = product_photo_url,
                            product_category            = category_model,
                            product_is_OEM              = is_OEM,
                            product_OEM                 = product_OEM   
                        )
                        new_product.save()

            for row in sheet2.rows:
	            v_types.append(row)
            for e in v_types:
                if e[2].value == 'Model':
                    pass
                else:
                    sku = e[0].value
                    make = e[1].value
                    model = e[2].value
                    year_from = e[3].value
                    year_to = e[4].value
                    vehicle_type = e[5].value 
                    brand = e[6].value
                    if Product.objects.filter(product_SKU = sku):
                        Category_add = Category_add + 1
                        find = find_a_part(make, model, year_from, year_to, vehicle_type, sku, brand)
                        find = find.values('id')[0]['id']
                        Product.objects.get(product_SKU = sku).product_find_part.add(find)
            return render(request, 'staff/excel.html', {'message':f'You Added {product_add} Products and {Category_add} Categories'})
        else:
           return render(request, 'staff/excel.html', {'message':'You Must to Submit A Excel File with ".xlsx" As Extention'}) 
    return render(request, 'staff/excel.html')




















