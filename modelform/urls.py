from django.conf.urls import url
from modelform import views

urlpatterns = [
    url(r'^$', views.modelform, name='modelform'),
    ]