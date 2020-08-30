from django.urls import path, include
from . import views

urlpatterns = [
    path('oldindex', views.index, name='index'),
    path('', views.home_view, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
