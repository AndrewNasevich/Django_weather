from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('pogoda', views.pogoda,name='pogoda'),

]