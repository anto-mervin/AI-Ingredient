from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('search/', views.search_grocery, name='search_grocery'),
    # path('recipe/', views.recipe_search, name='recipe_search'),
    # path('cart/', views.view_cart, name='view_cart'),
    # path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]
