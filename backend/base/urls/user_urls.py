from django.urls import path
# from base.views import user_views as views
from .. import views

urlpatterns = [
    path('test', views.index, name='test-groups'),
      
]