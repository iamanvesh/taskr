from django.conf.urls import include, url

from tasks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
