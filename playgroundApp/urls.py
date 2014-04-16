from django.conf.urls import patterns, url

from playgroundApp import views

urlpatterns=patterns('',
	url(r'^$', views.Playground_List, name='playgroundapp_home'),
	url(r'^playgroundapp/playground_info/(?P<pk>\d+)$', views.playgroundDetail, name='playground_info'),
        url(r'^playgroundapp/playground_suggest$', views.suggestPlayground, name='userSuggest'),
	url(r'^playgroundapp/user_profile$', views.userProfile, name='userProfile'),
	url(r'^playgroundapp/user_suggest$', views.userSuggest, name='userSuggest'),
	url(r'^playgroundapp/user_signup$', views.userSignUp, name='userSignUp'),
	url(r'^playgroundapp/user_login$', views.userLogin, name='userLogin'),

        #urls for the suggest a playground page
        url(r'playground_suggest.html', views.suggestPlayground, name='post_form_suggest'),
        url(r'^playgroundapp/map$', views.map, name='map'),

)