from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile),
    path('userinformation/', views.updateuserinformation),
    path('user/', views.currentuser),
    path('withdraw/', views.withdraw),
]
