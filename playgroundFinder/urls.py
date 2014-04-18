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
    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),
)
