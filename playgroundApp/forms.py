from django import forms
from playgroundApp import models

class login (forms.Form):
       name = forms.CharField(max_length=50)

#class addReviewForm (forms.Form):
      #name = forms.CharField(max_length=50)
      
class playgroundSuggest (forms.ModelForm):
	class Meta:
		model = models.SuggestPlayground