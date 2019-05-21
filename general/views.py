from django.shortcuts import render
from django.db import connections

# Create your views here.

from django.http import HttpResponse


def index(request):

     return render(request, 'general/index.html', {} )


