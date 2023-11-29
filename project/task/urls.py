from django.urls import path, re_path
from .views import error, index

urlpatterns = [

    path('', index),
    re_path(r'^error/', error),
]



