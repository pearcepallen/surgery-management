from django.urls import path
from base.views import room_views as views

urlpatterns = [
    path('', views.getRooms, name='rooms'),

    path('<str:pk>', views.getRoom, name='room'),  

    path('<str:pk>/surgeries', views.getSurgeries, name='room-surgeries'),  
]