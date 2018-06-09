from django import forms


class DepartmentForm(forms.Form):
    department_name = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    number = forms.IntegerField()
    postal_code = forms.IntegerField()
    contact_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    telephone = forms.CharField(max_length=50)
    telephone_2 = forms.CharField(max_length=50, required=False)


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)

