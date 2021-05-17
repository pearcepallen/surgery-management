from django.urls import path
from base.views import surgery_views as views

urlpatterns = [
    path('', views.getSurgeries, name='surgeries'),

    path('<str:pk>/', views.getSurgery, name='surgery'),    

    path('<str:pk>/doctors/', views.getSurgeryDoctors, name='surgery-doctors'),
]