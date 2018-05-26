from django import forms
from portfolio.models import message

class contact_form(forms.ModelForm):
	name = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(max_length=50, required=True)
	
	class Meta:
		model = message
		fields = ['name', 'email', 'website', 'text']
