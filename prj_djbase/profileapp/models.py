from django.db import models
from django.contrib.auth.models import User

# Create your models here.






# M2M Relationship
# class Vendor(models.Model):
# 	name = models.CharField(max_length=200)
# 	categories = models.ManyToManyField("Category",
# 				through="VendorCategory",
# 				related_name='vendors')
	
# 	class Meta:
# 		verbose_name_plural = "vendors"

# 	def __str__(self):
# 		return self.name

# class Category(models.Model):
# 	name = models.CharField(max_length=200)

# 	class Meta:
# 		verbose_name_plural = "categories"

# 	def __str__(self):
# 		return self.name


# class VendorCategory(models.Model):
# 	vendor = models.ForeignKey(Vendor, related_name='vendor_category',
# 					default="OtherVendor", on_delete=models.SET_DEFAULT)
# 	category = models.ForeignKey(Category, related_name='vendor_category',
# 					default="OtherCategory", on_delete=models.SET_DEFAULT)
	
# 	class Meta:
# 		verbose_name_plural = "vendor categories"

# 	def __str__(self):
# 		return f"Vendor: {self.vendor} -- Category: {self.category}"
