from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'Master'
    number = 26
    context = {'page': page, 'number': number, 'projects': projecstList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projecstList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
    

# Create your views here.
