from django.forms import ModelForm
from .models import Employer, Departement

class Form_employer(ModelForm):
	class Meta:
		model=Employer
		fields=['first_name','last_name','phone_number','email','address','departement']

