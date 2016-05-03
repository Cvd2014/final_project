from django.conf.urls import url

import views

urlpatterns = [
    url(r'^store/$', views.store_list, name='store'),
    url(r'^store/(?P<id>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^store/new/$',views.new_product, name="new_product"),
    url(r'^store/(?P<id>\d+)/edit/$', views.edit_product, name='edit_product'),
    url(r'^store/(?P<id>\d+)/delete/$', views.delete_product, name='delete_product')
]