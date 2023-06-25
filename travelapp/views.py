from django.shortcuts import render

from travelapp.models import meet_team,Place


def index(request):
    obj =meet_team.objects.all()
    obj2=Place.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj2})
