from django.urls import path
from .views import main,calculate

urlpatterns = [
    path("",view=main,name="main"),
    path("calculate/",view=calculate,name='calculate')
]
