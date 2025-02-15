from myApp import views  # ✅ Use absolute import
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
]