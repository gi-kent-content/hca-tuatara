from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from urllib.parse import unquote
import json

from .models import *

# Create your views here (except API views go in api.py)

def index(request):
    template = loader.get_template('hcat/home_page.html')
    context = {}
    return HttpResponse(template.render(context,request))

def project_all(request):
    project_list = Project.objects.order_by('short_name')
    project_dict = {'projects': project_list}
    return render(request, 'hcat/projectAll_page.html', context=project_dict)

def covid_projects(request):
    covid_list = Project.objects.filter(tags__tag__contains="COVID-19")
    covid_dict = {'covid_projects': covid_list}
    return render(request, 'hcat/covid19_page.html', context=covid_dict)

def projectdetail(request, name_id):
    project_details = Project.objects.get(short_name=unquote(name_id))
    detail_dict = {'project': project_details}
    return render(request, 'hcat/project_detail.html', context=detail_dict)

# class ProjectListView(generic.ListView):
#     template_name = 'hcat/project_list.html'
#     context_object_name = 'project_list'
#
#     def get_queryset(self):
#         return Project.objects.order_by("-id")[:100]
#
# class ProjectDetailView(generic.DetailView):
#     model=Project
#     template_name = 'hcat/project_detail.html'
#     context_object_name = 'project'

