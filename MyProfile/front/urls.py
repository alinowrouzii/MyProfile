from django.urls import path
from front.views import index

urlpatterns = [
    path("", index),
]
