from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField
from django.urls import reverse

class Category(models.Model):
    vehicle_land                = models.CharField(max_length=50)
    vehicle_type                = models.CharField(max_length=50)
    category                    = models.CharField(max_length=50, blank=True, null=True)
    sub_category                = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.sub_category
    
    class Meta:
        db_table = 'categories'

class Find_a_Part(models.Model):
    vehicle_type                = models.CharField(max_length=250)
    make                        = models.CharField(max_length=250, blank=True, null=True)
    model                       = models.CharField(max_length=250, blank=True, null=True)  
    year                        = models.CharField(max_length=250, blank=True, null=True)
    brand                       = models.CharField(max_length=250, blank=True, null=True)  
    category                    = models.CharField(max_length=250, blank=True, null=True)  
    sub_category                = models.CharField(max_length=250, blank=True, null=True) 
    


class Product(models.Model):
    product_name                = models.CharField(max_length=250)
    product_SKU                 = models.CharField(max_length=250, unique=True)
    product_OEM                 = models.CharField(max_length=250, blank=True, null=True)
    product_is_OEM              = models.BooleanField(default=False)
    product_photo_url           = models.URLField() 
    product_price               = models.DecimalField(max_digits=15, decimal_places=2)
    product_sale_price          = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    product_short_description   = models.TextField(max_length=150, blank=True, null=True)
    product_description         = models.TextField()
    product_add_date            = models.DateField(auto_now_add=True)
    product_width               = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    product_height              = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    product_lenght              = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    product_weight              = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    slug                        = AutoSlugField(unique=True, always_update=False, populate_from="product_name")
    is_active                   = models.BooleanField(default=True)
    product_stock               = models.IntegerField(blank=True, null=True)
    product_category            = models.ForeignKey(Category, on_delete=CASCADE)
    product_find_part           = models.ManyToManyField(Find_a_Part) 

    def __str__(self):
        return self.product_name
    

    def get_absolute_url(self):
        return reverse("Product:product_detailview", kwargs={"slug": self.slug})

    def get_category_vehicle_land(self):
        category = self.product_category.vehicle_land
        return category
    
    def get_category_vehicle_type(self):
        category = self.product_category.vehicle_type
        return category
    
    def get_category_category(self):
        category = self.product_category.category
        return category
    
    def get_category_sub_category(self):
        category = self.product_category.sub_category
        return category
    
    class Meta:
        db_table = 'products'




    




