"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#def users_view(request):
#	return "some value"
from django.http import HttpResponse
from tasks.views import users_view,users_view1,users_view2,url_fun
from tasks2.views import tasks2_view
#def url_fun(request):
#	return HttpResponse("sdfdsf")



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^users2/', users_view2),
    #url(r'^users/', users_view), 
    #url(r'^users1/', users_view1), 
    url(r'^users2/', users_view),
    url(r'^users1/', users_view),
    url(r'^users/', users_view),
    url(r'^url123/', url_fun),
    url(r'^tasks2/', tasks2_view),


]
