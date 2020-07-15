from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
	name = models.CharField(max_length=200)	
	
	class Meta:
		verbose_name_plural = "vendors"

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name


class Certification(models.Model):
	title = models.CharField(max_length=200)
	vendor = models.ForeignKey(Vendor, related_name='vendors',
					default=3, on_delete=models.SET_DEFAULT)
	category = models.ForeignKey(Category, related_name='categories',
					default=3, on_delete=models.SET_DEFAULT)


	class Meta:
		verbose_name_plural = "certifications"

	def __str__(self):
		return self.title


class VendorCertification(models.Model):
	certification = models.ForeignKey(Certification, related_name='vendor_certs',
					default=3, on_delete=models.SET_DEFAULT)
	user = models.ForeignKey(User, related_name='vendor_certs',
					on_delete=models.CASCADE)
	issue_date = models.DateField()
	expiry_date = models.DateField()


	class Meta:
		verbose_name_plural = "vendor certifications"

	def __str__(self):
		if self.user.first_name or self.user.last_name:
			return f"{self.user.first_name} {self.user.last_name} - {self.certification.title}" 
		else:
			return f"User {self.user.id} - {self.certification.title}" 





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
