from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# this is the crud api view created by satyaprakash


class EmployeeListView(ListView):
    model = Employee


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['ename', 'eno', 'esal', 'eaddress']


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['ename', 'eno', 'esal']


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('see_list')