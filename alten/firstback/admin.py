from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "code",
        "name",
        "description",
        "price",
        "quantity",
        "inventory_status",
        "category",
        "image",
        "rating",
    )


admin.site.register(Product, ProductAdmin)
