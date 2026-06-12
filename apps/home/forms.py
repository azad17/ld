from django import forms
from .models import Departments

class DepartmentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Departments