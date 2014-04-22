# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from playgroundApp.models import Playground, Features, SchoolDistrict, Age, TransportationFeatures
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from playgroundApp.forms import playgroundSuggest, suggestTest, playgroundFilter
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
#from pygeocoder import Geocoder
import json

def testFilter(request):
	f = playgroundFilter(request.GET, queryset=Playground.objects.all())
	return render_to_response('playgroundApp/filterTest.html',{'filter': f})

def testCreate(request):
	if request.POST:
		form = suggestTest(request.POST)
		#I think this is where we would set the field for latLon
		if form.is_valid():
			address = form.cleaned_data['street']
			#latLon = Geocoder.geocode(address)
			#form.latLon= latLon
			form.save()
			return HttpResponseRedirect(reverse('playgroundapp_home'))
	else:
		form = suggestTest()
	args = {}
	args.update(csrf(request))

	args['form'] = form
	args['dropdown'] = SchoolDistrict.objects.all()
	return render_to_response('playgroundapp/create_playground.html', args)

def Playground_List(request):

	playgrounds = Playground.objects.all()
	f = playgroundFilter(request.GET, queryset=Playground.objects.all())
	context = {
		'filter': f,
		'playgrounds': playgrounds,
	}
	return render (request, "playgroundApp/home.html", context)

def userLogin(request):
	c = {}
	c.update(csrf(request))
	return render_to_response(reverse('userLogin'), c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect(reverse('userLoggedin'))
	else:
		return HttpResponseRedirect(reverse('invalid_login'))

def userLoggedin(request):
	return render_to_response("playgroundApp/user_loggedin.html",{'full_name':request.user.username})

def invalid_login(request):
	return render_to_response("playgroundApp/user_invalid.html")

def userLogout(request):
	auth.logout
	return render_to_response("playgroundApp/user_logout.html")
def userSignUp(request):
	return  render (request, "playgroundApp/userSignup.html")

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			#instead of form.save() you can do a number of different things to increase security (like
			#having an email sent to the user with a link for them to click)
			form.save()
			return HttpResponseRedirect('/playgroundapp/register_success')
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()

	return render_to_response('playgroundApp/register.html', args)

def register_success(request):
	return render_to_response('playgroundApp/register_success.html')

def playgroundGeoCodes(request):
	playgrounds = Playground.objects.all()
	context = {
		'playgrounds': playgrounds
	}
	return render (request, "playgroundApp/map.html", context)


def playgroundDetail (request, pk):
	playground = get_object_or_404(Playground, id=pk)
	'''
	features = Features.objects.all()
	features = features.filter(playgroundID=pk)
	features = features[0]
	'''

	schoolDistrict = SchoolDistrict.objects.all()
	schoolDistrict = schoolDistrict.filter(id= playground.schoolDistrictID)
	schoolDistrict = schoolDistrict[0]
	'''
	ages = Age.objects.all()
	ages = ages.filter(ageID = playground.ageID)
	ages = ages[0]

	transport = TransportationFeatures.objects.all().filter(playgroundID = playground.playgroundID)[0]
	'''
	context = {
		'playground':playground,
		'schoolDistrict':schoolDistrict,
		#'features':features,
		#'age':ages,
		#'transport':transport,
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