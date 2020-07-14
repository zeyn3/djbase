from django.contrib import admin
from profileapp.models import Vendor, Category, VendorCategory
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(VendorCategory)



