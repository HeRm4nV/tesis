from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities_types_list, name='activities_types_list'),
    path('<type>/', views.activities_list, name='activities_list'),
]
