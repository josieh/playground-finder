from django import forms
from playgroundApp import models
from models import Playground
import django_filters

class login (forms.ModelForm):
	class Meta:
	      model = models.User
#The login shouldn't pull from the model itself - it should be adding to one

class signup (forms.ModelForm):
	class Meta:
	      model = models.User

#class addReviewForm (forms.Form):
      #name = forms.CharField(max_length=50)
      
class playgroundSuggest (forms.ModelForm):
	class Meta:
	      model = models.Playground

class suggestTest (forms.ModelForm):
       class Meta:
              model = Playground

class playgroundFilter(django_filters.FilterSet):
       class Meta:
              model = Playground
              fields = ['swing', 'slide', 'monkeyBars', 'sandBox', 'field', 'picnicTable', 'bathrooms', 'changingStation', 'shade','basketballCourt', 'baseball']