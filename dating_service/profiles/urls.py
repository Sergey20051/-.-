from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  
    path('edit/', views.edit_profile, name='edit_profile'),  
    path('homepage/', views.homepage, name='homepage'),  
    path('some-other-path/', views.some_other_view, name='some_other_view'),  
]
