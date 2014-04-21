from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'playgroundFinder.views.home', name='home'),
    # url(r'^playgroundFinder/', include('playgroundFinder.foo.urls')),
    url(r'^', include('playgroundApp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^playgroundapp/login/$', 'playgroundApp.views.userLogin', name="userLogin"),
    url(r'^playgroundapp/auth/$', 'playgroundApp.views.auth_view', name="authView"),
    url(r'^playgroundapp/logout/$', 'playgroundApp.views.userLogout', name="userLogout"),
    url(r'^playgroundapp/loggedin/$', 'playgroundApp.views.userLoggedin', name="userLoggedin"),
    url(r'^playgroundapp/invalid/$', 'playgroundApp.views.invalid_login', name="invalid_login"),
    url(r'^playgroundapp/register/$', 'playgroundApp.views.register_user', name="register_user"),
    url(r'^playgroundapp/register_success/$', 'playgroundApp.views.register_success', name="register_success"),
)
