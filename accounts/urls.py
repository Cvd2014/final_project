import views
from django.conf.urls import url,include
from django.contrib import admin

admin.autodiscover()
urlpatterns = [

    url(r'^register/$', views.register, name='register'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'login/$', views.login,name='login'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'',include('social.apps.django_app.urls', namespace='social')),
    url(r'',include('django.contrib.auth.urls',namespace='auth'))

]



