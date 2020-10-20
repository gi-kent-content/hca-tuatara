from django.urls import path

from . import views
from . import api

app_name = 'hcat'
urlpatterns = [
    path('project/', views.project_all, name='project_all_list'),
    path('project/covid19/', views.covid_projects, name='covid_project_list'),
    path('project/GenomeBrowser', views.genome_browser_projects, name='gbrowser_project_list'),
    path('project/CellBrowser', views.cell_browser_projects, name='cbrowser_project_list'),
    path('project/<str:name_id>/', views.projectdetail, name='project_detail')
]

