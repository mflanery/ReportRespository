from django.contrib import admin

from reports.apps import ReportsConfig

from .models import Department, Report, ReportUser

admin.site.register(Report)
admin.site.register(ReportUser)
admin.site.register(Department)
# admin.site.register(ReportsConfig)