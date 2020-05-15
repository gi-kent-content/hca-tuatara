from django.urls import path

from . import views
from . import api

app_name = 'hcat'
urlpatterns = [
    path('project/', views.project_all, name='project_all_list'),
    path('project/covid19/', views.covid_projects, name='covid_project_list'),
    path('project/<str:name_id>/', views.projectdetail, name='project_detail')
]

