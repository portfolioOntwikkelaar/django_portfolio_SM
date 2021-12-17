from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projecstList = [
    {
        'id':'1',
        'title':'Webshop',
        'description':'Website die u wenst te kennen',
    },
    {
        'id':'2',
        'title':'Dubble',
        'description':'Wat we probeerden naappen van 2009 projects awards',
    },
    {
        'id':'3',
        'title':'Hashtags zoeker ',
        'description':'Wat we probeerden niet doen in 2010',
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html', {'project': projectObj})
    

# Create your views here.
