# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    # print '!'*50
    try:
        print request.session['num']
    except KeyError:
        request.session['num'] = 0
    return render(request, 'survey_app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['num'] += 1
        return redirect('/result')
    return redirect('/')

def result(request):
    return render(request, 'survey_app/result.html')

def goback(request):
    return redirect('/')
