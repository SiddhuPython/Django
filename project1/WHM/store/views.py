# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def warehouses_view(request):
    '''
    resp = """<html>
    <h1>WAREHOUSES</h1>
    <ul>
    <li>Ameer Pet</li>
    <li>SR Nagar</li>
    </ul>
    </html>
    """
    '''
    return render(request, 'store/warehouses.html')
def products_view(request):
    resp = """
    <html>
    <h1>Products</h1>
    <ul>
    <li>LED TV</li>
    <li>Iphone 6s</li>
    </ul>
    </html>
    """
    return HttpResponse(resp)
