from django.urls import path
from base.views import patient_views as views

urlpatterns = [
    path('', views.getPatients, name='patients'),

     path('<str:pk>', views.getPatient, name='patient'),

    # path('<str:pk>', views.getStaff, name='staff'),

    
]