from django import forms
from .models import Worker,Project

class AddWorker(forms.ModelForm):
    class Meta:
        model=Worker
        fields=["name","age","contact","designation"]

class AddProject(forms.ModelForm):
    class Meta:
        model=Project
        fields=["project_name","client_name","mobile","location","budget","s_date","status","e_date"]