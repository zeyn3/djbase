from django.contrib import admin
# 
# Register your models here.

# 1:M Setup
from profileapp.models import Vendor, Category, Certification, VendorCertification
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Certification)
admin.site.register(VendorCertification)


# M2m Relations
# from profileapp.models import Vendor, Category, VendorCategory
# admin.site.register(Vendor)
# admin.site.register(Category)
# admin.site.register(VendorCategory)
