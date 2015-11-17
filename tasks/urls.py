from django.conf.urls import include, url

from tasks import views

urlpatterns = [
    url(r'new', views.new_task, name='new_task'),
    url(r'^$', views.all_tasks, name='all_tasks'),
]
