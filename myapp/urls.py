from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('airecipe/', views.ai_recipe, name='ai_recipe'),
]
