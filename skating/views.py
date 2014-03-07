from skating.models import Athlete
from django.shortcuts import render, get_object_or_404

def home(request):
    context = {
        'athlete_count': Athlete.objects.count(),
        'athletes': Athlete.objects.all(),
    }
    return render(request, "skating/home.html", context)

def athlete(request, pk):
    context={
    'athletes': Athlete.objects.all(),
    'athlete': get_object_or_404(Athlete, id=pk),
    }
    return render(request, "skating/athlete.html", context)

def athleteList(request):
    athletes = Athlete.objects.all()
    return render(request, 'skating/athlete_list.html', {"athletes": athletes} )




