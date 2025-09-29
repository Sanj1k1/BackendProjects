from django.urls import path
from .views import random_quote,quote_page
urlpatterns = [
    path("", view=quote_page, name="quote_page"),
    path('api/quote/',view=random_quote,name="random_quote")
]