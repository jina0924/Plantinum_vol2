from django.urls import path
from . import views


urlpatterns = [
    path('main', views.Leaf82ListAPI.as_view()),
    path('new/', views.create_leaf82),
    path('search/sido/', views.search_sido),
    path('search/<sido>/sigungu/', views.search_sigungu),
    path('search', views.SearchAPI.as_view()),
    path('<username>/<int:posting_addr>/', views.detail_update_delete),
]
