from django.db import models
from django.db.models.deletion import PROTECT

class ReportUser(models.Model):
    external_user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # is_requester = models.BooleanField(default=0)
    # is_report_writer = models.BooleanField(default=0)
    department = models.ForeignKey(
        'Department',
        on_delete=PROTECT
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.external_user_id + ')'

    
class Report(models.Model):
    report_id = models.AutoField(
        primary_key=True
    )
    report_name = models.CharField(max_length=300)
    report_requester = models.ForeignKey(
        'ReportUser',
        null=True,
        on_delete=models.PROTECT,
        related_name='report_requestor_user'
    )
    report_description = models.CharField(max_length=1000)
    # report_requester_department = models.ForeignKey(
    #     'Department',
    #     on_delete=PROTECT, 
    #     blank=True,
    #     # default='1',
    # )
    report_writer = models.ForeignKey(
        'ReportUser',
        null=True,
        on_delete=PROTECT,
        related_name='report_writer_user'
    )

    def __str__(self):
        return self.report_name + ' (' + str(self.report_id) + ')'
    

class Department(models.Model):
    department_id = models.CharField(max_length=30)
    department_name = models.CharField(max_length=300)

    def __str__(self):
        return self.department_name + ' (' + self.department_id + ')'
    


