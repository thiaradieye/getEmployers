from django.db import models
from django.utils import timezone

# Create your models here.

class Departement (models.Model):
	name = models.CharField(max_length=200, verbose_name='Name',default="Informatique")

	class Meta:
		verbose_name_plural='Departement'

	def __str__(self):
		return self.name


class Employer (models.Model):
	first_name = models.CharField(max_length=50, verbose_name='First Name')
	last_name = models.CharField(max_length=50, verbose_name='Last Name')
	phone_number = models.CharField(max_length=21, verbose_name='Phone Number')
	email = models.EmailField(max_length=70, verbose_name='Email')
	address = models.CharField(max_length=100, verbose_name='Address')
	date_embauche = models.DateTimeField(default=timezone.now,verbose_name='Date Embauche')
	departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural='Employer'

	def __str__(self):
		return self.first_name

