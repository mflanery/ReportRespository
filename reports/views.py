import imp
from pyexpat import model
from urllib.request import Request
from django.forms import fields
from django.template import context
from .models import Report, Department
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession



def index(request):
    """View function for home page of the site"""
    num_reports = Report.objects.all().count()
    num_departments = Department.objects.all().count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_reports': num_reports,
        'num_departments': num_departments,
        'num_visits': num_visits,
    }

    return render(request, 'reports/index.html', context=context)



class ReportListView(ListView):
    model = Report


class ReportDetail(DetailView):
    model = Report

class ReportCreate(CreateView):
    model = Report
    fields = [
        "report_name",
        "report_requester",
        "report_writer",
        "report_description",
    ]
    success_url = "/list"


class ReportUpdateView(UpdateView):
    model = Report
    fields = [
        "report_name",
        "report_requester",
        "report_writer",
        "report_description"
    ]
    success_url = "/list"