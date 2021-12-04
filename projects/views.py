from django.shortcuts import render
from .models import Project
from .forms import ProjectFrom


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()   # Return all the tags related to a single project
    context = {
        'project': project,
        'tags': tags,
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectFrom()
    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)
