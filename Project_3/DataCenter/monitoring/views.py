# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def temparature_view(request):
	return HttpResponse("temparture is:") 
def cpu_usage_view(rquest):
	return HttpResponse("cpu_usage_view : ")
def storage_view(request):
	return HttpResponse("storage_view : ")

