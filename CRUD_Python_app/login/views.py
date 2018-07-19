# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Users


# Create your views here.


def index(request):
    # return HttpResponse('Hello from Land Page')
    all_users = Users.objects.all()
    return render(request, 'login/index.html', {'all_users': all_users})
