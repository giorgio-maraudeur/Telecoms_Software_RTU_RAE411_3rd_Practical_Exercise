from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Hello_index2),
]