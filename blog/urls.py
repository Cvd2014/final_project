from django.conf.urls import url

import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='blog'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail, name='blog_detail'),
    url(r'^post/new/$',views.new_post, name="new_post"),
    url(r'^blog/(?P<id>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^blog/(?P<id>\d+)/delete/$', views.delete_post, name='delete_post')
]