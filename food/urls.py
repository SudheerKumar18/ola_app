from food.views import *
from django.urls import path

urlpatterns=[
    path('nonveg/',nonveg,name='nonveg'),
]