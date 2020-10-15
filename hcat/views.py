from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import unquote
from .models import Project, SuggestedProjects
from .suggestion_form import ProjectSuggestion
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

def genome_browser_projects(request):
    gbrowser_list = Project.objects.filter(tags__tag__contains="genome browser")
    gbrowser_dict = {'gbrowser_projects': gbrowser_list}
    return render(request, 'hcat/gbrowser_page.html', context=gbrowser_dict)

def projectdetail(request, name_id):
    project_details = Project.objects.get(short_name=unquote(name_id))
    detail_dict = {'project': project_details}
    return render(request, 'hcat/project_detail.html', context=detail_dict)


def project_suggestion(request):
    form = ProjectSuggestion()
    if request.method == 'POST':
        form = ProjectSuggestion(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            sname = form.cleaned_data['submitter_name']
            links = form.cleaned_data['links']
            summary = form.cleaned_data['summary']

            project = SuggestedProjects(title=title, submitter_name=sname, links=links,
                                        summary=summary, ip_address=request.META['REMOTE_ADDR'])
            project.save()
            return HttpResponseRedirect('/')
        else:
            print('Error in form')
    return render(request, 'hcat/project_suggestion_form.html', {'form': form})

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

