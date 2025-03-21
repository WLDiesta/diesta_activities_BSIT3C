from myApp import views  # ✅ Use absolute import
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/items/', views.get_items, name='get_items'),
    path('api/items/search/', views.search_items, name='search_items'),
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
    path('api/items/add/', views.add_item, name='add_item'),
    path('api/items/update/<int:item_id>/', views.update_item, name='update_item'),
    path('api/items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]