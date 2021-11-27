from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    return HttpResponse('This is the ALL projects page')


def project(request, pk):
    return HttpResponse('This is a SINGLE project page' + ' ' + str(pk))
