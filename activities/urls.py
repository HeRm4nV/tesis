from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities_types_list, name='activities_types_list'),
    path('<type>/', views.activities_list, name='activities_list'),
    path('sources/<activityName>.html', views.sources, name='sources'),
    path('js/<activityName>.js', views.js, name='JavaScript'),
]
