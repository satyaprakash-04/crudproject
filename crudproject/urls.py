"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('$', views.EmployeeListView.as_view(), name='see_list'),
    url('detail/(?P<pk>\d+)/$', views.EmployeeDetailView.as_view(), name='get_data'),
    url('update/(?P<pk>\d+)$', views.EmployeeUpdateView.as_view()),
    url('create/', views.EmployeeCreateView.as_view()),
    url('delete/(?P<pk>\d+)/$', views.EmployeeDeleteView.as_view()),
]
