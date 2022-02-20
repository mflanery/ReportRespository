from django.contrib import admin
from django.urls import path, include

from reports.models import Report
from . import views
from .views import ReportListView
from .views import ReportDetail
from .views import ReportUpdateView, ReportCreate
from .views import index
import reports

app_name = 'reports'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:report_id>/edit_report/',views.edit_report, name='edit_report'),
    # path('edit_report/',views.edit_report, name='edit_report'),
    # path('report_list/',views.report_list, name='report_list'),
    # path('<int:report_id>/get_report/', views.get_report, name='get_report'),
    path('list', ReportListView.as_view(), name='reportlist'),
    path('<pk>/update', ReportUpdateView.as_view(), name='update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<pk>/', ReportDetail.as_view(), name='ReportDetail'),
    path('create', ReportCreate.as_view(), name='create'),
]

