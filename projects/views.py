from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'Master cleanse retro brunch keytar dreamcatcher, 90s sriracha hammock.'
    number = 26
    context = {'page': page, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html')
    

# Create your views here.
