from django import forms
class login (forms.Form):
       name=forms.CharField(max_length=50)

class suggestForm (forms.Form):
      name = forms.CharField(max_length=50)
      
