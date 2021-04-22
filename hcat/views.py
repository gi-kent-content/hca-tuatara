from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import unquote
from .models import Project, SuggestedProjects
from .suggestion_form import ProjectSuggestion
from .new_project_form import NewProject, AddTag, AddOrgan, AddOrganPart, AddDisease, AddLab, AddPub, AddUrl, AddContributors, AddLibPrep
import json

from .models import *

# Create your views here (except API views go in api.py)

def index(request):
    template = loader.get_template('hcat/home_page.html')
    context = {}
    return HttpResponse(template.render(context,request))

def project_all(request):
    project_list = Project.objects.order_by('short_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(project_list, 15)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'hcat/projectAll_page.html', {'projects': projects})

def covid_projects(request):
    covid_list = Project.objects.filter(tags__tag__contains="COVID-19").order_by('short_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(covid_list, 15)

    try:
        covid_projs = paginator.page(page)
    except PageNotAnInteger:
        covid_projs = paginator.page(1)
    except EmptyPage:
        covid_projs = paginator.page(paginator.num_pages)

    return render(request, 'hcat/covid19_page.html', {'covid_projects': covid_projs})

def genome_browser_projects(request):
    gbrowser_list = Project.objects.filter(tags__tag__contains="genome browser").order_by('short_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(gbrowser_list, 15)

    try:
        gbrowser_projs = paginator.page(page)
    except PageNotAnInteger:
        gbrowser_projs = paginator.page(1)
    except EmptyPage:
        gbrowser_projs = paginator.page(paginator.num_pages)

    return render(request, 'hcat/gbrowser_page.html', context={'gbrowser_projects': gbrowser_projs})

def projectdetail(request, name_id):
    project_details = Project.objects.get(short_name=unquote(name_id))
    detail_dict = {'project': project_details}
    return render(request, 'hcat/project_detail.html', context=detail_dict)

def cell_browser_projects(request):
    cbrowser_list = Project.objects.filter(tags__tag__contains="cell browser").order_by('short_name')
    page = request.GET.get('page', 1)
    paginator = Paginator(cbrowser_list, 15)

    try:
        cbrowser_projs = paginator.page(page)
    except PageNotAnInteger:
        cbrowser_projs = paginator.page(1)
    except EmptyPage:
        cbrowser_projs = paginator.page(paginator.num_pages)

    return render(request, 'hcat/cbrowser_page.html', context={'cbrowser_projects': cbrowser_projs})

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

@login_required
def new_project(request):
    form = NewProject(prefix="np")
    tag_form = AddTag(prefix="tag")
    organ_form = AddOrgan(prefix="organ")
    opart_form = AddOrganPart(prefix="opart")
    disease_form = AddDisease(prefix="disease")
    lib_prep_form = AddLibPrep(prefix="lib_prep")
    lab_form = AddLab(prefix="lab")
    pub_form = AddPub(prefix="pub")
    contrib_form = AddContributors(prefix="contrib")
    url_form = AddUrl(prefix="url")
    if request.method == 'POST':
        if 'fullsubmit' in request.POST:
            form = NewProject(request.POST, prefix="np")
            if form.is_valid():
                form.save()
                name_id = request.POST.get('np-short_name')
                return redirect('hcat:project_detail', name_id=name_id)
            else:
                print('Error in form')
        elif 'tagSubmit' in request.POST:
            tag_form = AddTag(request.POST, prefix="tag")
            if tag_form.is_valid():
                tag_form.save()
            else:
                print('Error in form')
        elif 'organSubmit' in request.POST:
            organ_form = AddOrgan(request.POST, prefix="organ")
            if organ_form.is_valid():
                organ_form.save()
            else:
                print('Error in form')
        elif 'opartSubmit' in request.POST:
            opart_form = AddOrganPart(request.POST, prefix="opart")
            if opart_form.is_valid():
                opart_form.save()
            else:
                print('Error in form')
        elif 'diseaseSubmit' in request.POST:
            disease_form = AddDisease(request.POST, prefix="disease")
            if disease_form.is_valid():
                disease_form.save()
            else:
                print('Error in form')
        elif 'LibprepSubmit' in request.POST:
            lib_prep_form = AddLibPrep(request.POST, prefix="lib_prep")
            if lib_prep_form.is_valid():
                lib_prep_form.save()
            else:
                print('Error in form')
        elif 'labSubmit' in request.POST:
            lab_form = AddLab(request.POST, prefix="lab")
            if lab_form.is_valid():
                lab_form.save()
            else:
                print('Error in form')
        elif 'pubSubmit' in request.POST:
            pub_form = AddPub(request.POST, prefix="pub")
            if pub_form.is_valid():
                pub_form.save()
            else:
                print('Error in form')
        elif 'contribSubmit' in request.POST:
            contrib_form = AddContributors(request.POST, prefix="contrib")
            if contrib_form.is_valid():
                contrib_form.save()
            else:
                print('Error in form')
        elif 'urlSubmit' in request.POST:
            url_form = AddUrl(request.POST, prefix="url")
            if url_form.is_valid():
                url_form.save()
            else:
                print('Error in form')
    return render(request, 'hcat_will/new_project_sub.html', {'form': form, 'tag_add': tag_form, 'organ_add': organ_form,
                                                              'opart_add': opart_form, 'disease_add': disease_form,
                                                              'lib_prep_add': lib_prep_form, 'lab_add': lab_form,
                                                              'pub_add': pub_form, 'contrib_add': contrib_form,
                                                              'url_add': url_form})

