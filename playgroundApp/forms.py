from django import forms
from playgroundApp import models

class login (forms.ModelForm):
	class Meta:
		model = models.User
#The login shouldn't pull from the model itself - it should be adding to one

#class signup (forms.ModelForm):
	#class Meta:
		#model = models.User

#class addReviewForm (forms.Form):
      #name = forms.CharField(max_length=50)
      
class playgroundSuggest (forms.ModelForm):
	class Meta:
		model = models.SuggestPlayground

