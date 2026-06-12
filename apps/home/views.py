from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from .forms import DepartmentForm
from django.http import HttpResponse
from apps.team.models import *
from apps.accounts.models import *
from django.db import connection, reset_queries
from .models import *
from django.urls import reverse_lazy

# Create your views here.

class HomeView(View):

    def get(self, request):
        reset_queries()
        # for career in Career.objects.select_related('user'):
        #     print(career.user.email)
        #     print(len(connection.queries))
        for car in Career.objects.select_related('user','club'):
                print(car.user.email)
                print(car.club.name)
                print(len(connection.queries)) 
        return HttpResponse("hey")


class DepartmentCreateView(CreateView):
    model = Departments
    form_class = DepartmentForm
    template_name = 'home/department.html'
    success_url = reverse_lazy("department")

# class DepartmentViewSet(ModelViewSet):
#     queryset = Departments.objects.all()
#     serializer = DepartmentSerializer()
#     permission_class = [IsAuthenticated]