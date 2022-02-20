from django import forms
from django.db.models import fields
from .models import Report

# class ReportEditForm(forms.Form):
#     report_name = forms.CharField(max_length=300)
#     report_requester = forms.CharField(max_length=300)

class ReportEditForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"


        

