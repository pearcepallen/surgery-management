from django.urls import path
from base.views import staff_views as views

urlpatterns = [
    path('', views.createStaff, name='staff-create'),
    path('<str:pk>', views.getStaff, name='staff'),
]