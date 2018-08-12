# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import requests
# Create your views here.
def upcoming(request):
    response = requests.get('https://contesttrackerapi.herokuapp.com/android/')
    data = response.json()
    upcoming = data['result']['upcoming']
    return render(request, 'upcoming.html', {'upcoming':upcoming, "title": "Programers Calender"})

def ongoing(request):
    response = requests.get('https://contesttrackerapi.herokuapp.com/android/')
    data = response.json()
    ongoing = data['result']['ongoing']
    return render(request, 'ongoing.html', {'ongoing':ongoing, "title": "Programers Calender"})

def home(request):
    return render(request, 'home.html', {"title": "Programmer\'s Calender"})
