from django.urls import path
from django.conf.urls import url
from stocks import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/date/', views.indexQuery, name='indexQuery')
]