from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('reset', views.resetUserPassword, name='reset-password'),
    path('new', views.setNewPassword, name='set-password'),
    # Add logout
      
]