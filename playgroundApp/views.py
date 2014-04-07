# Create your views here.
#from django.http import render, get_object_or_404, redirect, render_to_response
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from playgroundApp.models import Playground, UserReview
from playgroundApp.forms import addReviewForm


def Playground (request):
	#Playerground=get_object_or_404 (Playground, id=pk)
	#return render (request, 'playgroundApp/playground_info.html', {"Playground": Playground})
	return render (request, "playgroundApp/playground_info.html")
def Playground_List(request):
	#playground_list=Playground.object.all()
	#paginator=Paginator(playground_list, 10)
	#page=request.GET.get('page')

	#try:
		#playgrounds=paginator.page(page)
	#except PageNotAnInteger:
		#playgrounds=paginator.page(1)
	#except Emptypage:
		#playgrounds=paginator.page(paginator.num_pages)
	#return render (request, 'playgroundApp/playground_list.html' {playgrounds: playgrounds})
	return render (request, "home.html")

def suggestPlayground(request):
	#if request.method == 'GET':
		#form=addPlaygroundForm()
	#else:
		#form=addPlaygroundForm(request.POST)
		#submitDate = datetime.utcnow
		#if form.is_valid():
			#Name=form.cleaned_data['Name']
			#Street=form.cleaned_data['Street']
			#Zipcode=form.cleaned_data['Zipcode']
			#Handicap=form.cleaned_data['Handicap']
			#isCertifield=form.cleaned_data['isCertifield']
			#Image=form.cleaned_data['Image']
			#GeoCoordinateLat=form.cleaned_data['GeoCoordinateLat']
			#GeoCoordinateLon=form.cleaned_data['GeoCoordinateLon']
			#Playground=Playground.objects.create(Name=Name, Street=Street, Zipcode=Zipcode, Handicap=Handicap, isCertifield=isCertifield, Image=Image, GeoCoordinateLat=GeoCoordinateLat, GeoCoordinateLon=GeoCoordinateLon, Date=submitDate)
			#return HttepResponseRedirect (reverse('Playground_list'))

	#return render (request, 'playgroundApp/new_playground.html', { 'form': form, })
	return render (request, "playgroundApp/playgroundSuggest.html")
def userProfile (request):
	return (request, "playgroundApp/userProfile.html")
	#User=get_object_or_404 (Playground)
        #return render (request, 'playgroundApp/user_info.html', {"User": User})

def userLogin (request):
	
	if request.method=='POST':
		form=login()
	else:
		form=login(request.GET)
	if form.is_valid():
		User=User.objects.all().filter(name=form.clean_data['name'])
		return render (request, "playgroundApp/user_profile.html", {'User': User})
	
	return render (request, "playgroundApp/user_login.html", {'form': form,})

def userSignUp(request):
	return  render (request, "plagyroundApp/userSignup.html")

def home(request):
        return HttpResponse('HelloWorld')

# Below is copied from Xing with comments taken out
# Create your views here.

from django.shortcuts import render, render_to_response


def playgroundDetail (request):
	return render (request, "playgroundApp/playground_info.html")

def playgroundList(request):
	return render (request, "playgroundApp/home.html")

def suggestPlayground(request):
	return render (request, "playgroundApp/playground_suggest.html")

def userProfile (request):
	return render (request, "playgroundApp/user_profile.html")

def userLogin (request):
	return render (request, "playgroundApp/user_login.html")

def userSignUp(request):
	return  render (request, "playgroundApp/user_signup.html")

def userSuggest(request):
	return  render (request, "playgroundApp/user_suggest.html")

#view for when the user wants to post a review of a playground
def userReview(request):
	if request.method == 'GET':
		newReview = addReviewForm()
	else:
		newReview =addReviewForm(request.POST)
		submitdate =datetime.utcnow()
	if newReview.is_valid():
		newReview =UserReview.objects.create(name=request.POST['name'], date=submitdate)
		return HttpResponseRedirect(reverse('playgroundapp_home'))
	return render(request, 'playgroundApp/new_review.html')


def map(request):
	return  render (request, "playgroundApp/map.html")

