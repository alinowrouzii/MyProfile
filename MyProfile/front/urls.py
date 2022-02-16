from django.urls import path
from front.views import index, post

urlpatterns = [
    path("", index, name="index"),
    path("post/<pk>/", post, name="post-item"),
]
