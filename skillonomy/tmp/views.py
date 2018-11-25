from django.shortcuts import render
from tmp.models import *
# Create your views here.


def index(request):
    curs = Curs.objects.all()
    return render(request, 'tmp/home.html')

def explore_courses(request):
    curs = Curs.objects.all()
    return render(request, 'tmp/explore_courses.html')


