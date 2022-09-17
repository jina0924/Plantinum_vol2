from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants),
    # path('all', views.MemoList.as_view()),
    path('search/', views.search_all),
    path('search/<plantname>/', views.search),
    path('myplant/', views.create_myplant),
    path('myplant/<username>/', views.read_myplant),
    path('myplant/<int:myplant_pk>/otp/', views.create_otp),
    path('myplant/<int:myplant_pk>/otp/status/', views.otp_status),
    path('myplant/<int:myplant_pk>/disconnect/', views.disconnect),
    path('myplant/<int:myplant_pk>/detail/', views.detail),
    path('myplant/<int:myplant_pk>/diary/', views.diary),
    path('myplant/<int:myplant_pk>/otp/remove/', views.otp_remove),
]
