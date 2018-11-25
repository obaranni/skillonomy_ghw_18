from django.shortcuts import render
from tmp.models import *
# Create your views here.


def index(request):
    curs = Curs.objects.all()
    return render(request, 'tmp/home.html')

def explore_courses(request):
    curs = Curs.objects.all()
    curs_image = [str(x.image)[3::] for x in curs]
    return render(request, 'tmp/explore_courses.html', {"courses": curs_image})

def profile(request):
    curs = Curs.objects.all()
    return render(request, 'tmp/profile.html')



