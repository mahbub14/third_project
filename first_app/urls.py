from django.urls import path,include
from . import views
urlpatterns = [
    path('card/', views.card),
    
]