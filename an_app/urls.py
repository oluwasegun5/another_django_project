from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.greet),
    path('ind', views.index),
]
