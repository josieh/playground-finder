# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from playgroundApp.models import Playground
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from playgroundApp.forms import playgroundSuggest
from django.core.urlresolvers import reverse
import json

def Playground_List(request):
	
	playgrounds = Playground.objects.all()
	context = {
		'playgrounds': playgrounds
	}
	return render (request, "playgroundApp/home.html", context)


def userProfile (request):
        return (request, "playgroundApp/userProfile.html")
#User=get_object_or_404 (Playground)
#return render (request, 'playgroundApp/user_info.html', {"User": User})
	
def userLogin (request):
	if request.method=='GET':
		formLogin=login()
	else:
		formLogin=login(request.GET)
	if formLogin.is_valid():
		User=User.objects.all().filter(name=formLogin.clean_data['name'])
		return render (request, "playgroundApp/user_profile.html", {'User': User})
	return render (request, "playgroundApp/user_login.html", {'form': formLogin,})

def userSignUp(request):
	return  render (request, "playgroundApp/userSignup.html")

def playgroundGeoCodes(request):
	playgrounds = Playground.objects.all()
	context = {
		'playgrounds': playgrounds
	}
	return render (request, "playgroundApp/map.html", context)



def playgroundDetail (request, pk):
	playground = get_object_or_404(Playground, id=pk)
	
	features = Features.objects.all()
	features = features.filter(playgroundID=pk)
	features = features[0]
	
	
	schoolDistrict = SchoolDistrict.objects.all()
	schoolDistrict = schoolDistrict.filter(schoolDistrictID = playground.schoolDistrictID)
	schoolDistrict = schoolDistrict[0]
	
	ages = Age.objects.all()
	ages = ages.filter(ageID = playground.ageID)
	ages = ages[0]
	
	context = {
		'playground':playground,
		'schoolDistrict':schoolDistrict,
		'features':features,
		'age':ages,
	}
	return render (request, "playgroundApp/playground_info.html", context)

def playgroundList(request):
	return render (request, "playgroundApp/home.html")

def suggestPlayground(request):
        return render(request, 'playgroundApp/playground_suggest.html')

'''def formSuggest(request):
        if request.method == 'GET':
               formSuggestion = playgroundSuggest()
        else:
               formSuggestion = playgroundSuggest(request.POST)
               submitdate =datetime.utcnow()
               if formSuggestion.is_valid():
                        playgroundName = formSuggestion.cleaned_data['playgroundName']
                        address = formSuggestion.cleaned_data['address']
                        description = formSuggestion.cleaned_data['description']
                        suggest =suggestPlayground.objects.create(name=request.POST['name'], address=request.POST['address'], description=request.POST['description'])
                        return HttpResponseRedirect(reverse('playgroundapp_home'))
        return render(request, 'playgroundApp/playground_suggest.html', { 'form': formSuggestion, })'''
        
def formSuggest(request):
        if request.method == 'GET':
               formSuggestion = playgroundSuggest()
        else:
               formSuggestion = playgroundSuggest(request.POST)
               submitdate =datetime.utcnow()
               if formSuggestion.is_valid():
                        playgroundName = formSuggestion.cleaned_data['playgroundName']
                        address = formSuggestion.cleaned_data['address']
                        description = formSuggestion.cleaned_data['description']
                        suggest =suggestPlayground.objects.create(name=request.POST['name'], address=request.POST['address'], description=request.POST['description'])
                        return HttpResponseRedirect(reverse('playgroundapp_home'))
        return render(request, 'playgroundApp/playground_suggest.html', { 'formSuggest': formSuggestion, })

def userProfile (request):
	return render (request, "playgroundApp/user_profile.html")

def userLogin (request):
	return render (request, "playgroundApp/user_login.html")

def userSignUp(request):
	return  render (request, "playgroundApp/user_signup.html")


'''def userReview(request):
       if request.method == 'GET':
               newReview = addReviewForm()
       else:
               newReview =addReviewForm(request.POST)
               submitdate =datetime.utcnow()
       if newReview.is_valid():
               newReview =UserReview.objects.create(name=request.POST['name'], date=submitdate)
               return HttpResponseRedirect(reverse('playgroundapp_home'))
       return render(request, 'playgroundApp/new_review.html')
'''

def userSuggest(request):
       if request.method == 'GET':
               newSuggest = addReviewForm()
       else:
               newSuggest =addPlayground(request.POST)
               submitdate =datetime.utcnow()
       if newSuggest.is_valid():
               newRenewSuggestview =UserReview.objects.create(name=request.POST['name'], date=submitdate)
               return HttpResponseRedirect(reverse('playgroundapp_home'))
       return render(request, 'playgroundApp/user_suggest.html')

def map(request):
        return render (request, "playgroundApp/map.html")
        
