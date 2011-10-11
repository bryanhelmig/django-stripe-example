from django.conf.urls.defaults import *
from sales import views

urlpatterns = patterns('',
    url(r'^charge/$', views.charge, name="charge"),
)