from django import forms

# this is a python/html form that is a simplier way of getting data through a text box and storing it vs a standard text box on its own

class CreateNewCart(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

