from django.conf.urls import include, url

from common import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
