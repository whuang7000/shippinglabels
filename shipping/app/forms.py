from django import forms

class AddressForm(forms.Form):
	company = forms.CharField(label='Company', max_length=100, required=False)
	street_1 = forms.CharField(label='Address Line 1', max_length=100)
	street_2 = forms.CharField(label='Address Line 2', max_length=100, required=False)
	city = forms.CharField(label='City', max_length=100)
	state = forms.CharField(label='State', max_length=2)
	zip_code = forms.CharField(label='Zip', max_length=100)
	name = forms.CharField(label='Name', max_length=100)


class ParcelForm(forms.Form):
	length = forms.DecimalField(label='Length', max_digits=10, decimal_places=3)
	width = forms.DecimalField(label='Width', max_digits=10, decimal_places=3)
	height = forms.DecimalField(label='Height', max_digits=10, decimal_places=3)
	weight = forms.DecimalField(label='Weight', decimal_places=3)