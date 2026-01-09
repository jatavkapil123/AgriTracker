from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farm/<int:farm_id>/', views.farm_detail, name='farm_detail'),
    path('crop/<int:crop_id>/', views.crop_detail, name='crop_detail'),
    path('farm/<int:farm_id>/add-crop/', views.add_crop, name='add_crop'),
    path('irrigation/', views.irrigation_dashboard, name='irrigation_dashboard'),
    path('irrigation/<int:irrigation_id>/complete/', views.complete_irrigation, name='complete_irrigation'),
    path('guide/', views.crop_guide, name='crop_guide'),
]