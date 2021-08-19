from django.conf.urls import url
from modelform import views

urlpatterns = [
    url(r'^$', views.modelform, name='modelform'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^ecommerce$', views.ecommerce, name='ecommerce'),
    ]