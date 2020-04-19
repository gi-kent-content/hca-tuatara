from django.urls import path

from . import views
from . import api

app_name = 'hcat'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project', views.ProjectListView.as_view(), name='project_list'),
    path('project/', views.project_all, name='project_all_list'),
    path('project/covid19/', views.covid_projects, name='covid_project_list')
]

