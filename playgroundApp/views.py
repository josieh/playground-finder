# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from playgroundApp.models import Playground
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from playgroundApp.forms import playgroundSuggest
from django.core.urlresolvers import reverse
import json

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
	playgrounds = Playground.objects.all()
	context = {
		'playgrounds': playgrounds
	}
	#playgrounds = Playground.objects.all()
	#playgrounds_json = json.dumps(playgrounds)
	#context2 = {
		#'playgrounds_json':playgrounds_json
	#}
	#return render (request, "home.html", context2)
	return render (request, "playgroundApp/home.html", context)


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

# Below is copied from Xing with comments taken outh


# Create your views here.

from django.shortcuts import render, render_to_response


def playgroundDetail (request):
	return render (request, "playgroundApp/playground_info.html")

def playgroundList(request):
	return render (request, "playgroundApp/home.html")

def suggestPlayground(request):
	if request.method == 'GET':
               form = playgroundSuggest()
        else:
               form =playgroundSuggest(request.POST)
               submitdate =datetime.utcnow()
               if form.is_valid():
                        playgroundName = form.cleaned_data['playgroundName']
                        address = form.cleaned_data['address']
                        description = form.cleaned_data['description']
                        suggest =suggestPlayground.objects.create(name=request.POST['name'], address=request.POST['address'], description=request.POST['description'])
                        return HttpResponseRedirect(reverse('playgroundapp_home'))
        return render(request, 'playgroundApp/playground_suggest.html', { 'form': form, })

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
        
