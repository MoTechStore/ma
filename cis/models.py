from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import os
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from rms.models import User



class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500,blank=True, null=True)
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)


       
class Task(models.Model):
    task_title = models.CharField(max_length=500,blank=True, null=True)
    task_customer = models.CharField(max_length=500,blank=True, null=True)
    supervisor = models.CharField(max_length=500,blank=True, null=True)
    task_desc = models.CharField(max_length=500,blank=True, null=True)
    amount = models.CharField(max_length=500,blank=True, null=True)
    modus = models.CharField(max_length=500,blank=True, null=True)
    comment = models.CharField(max_length=500,blank=True, null=True)
    suspect = models.CharField(max_length=500,blank=True, null=True)
    status = models.CharField(max_length=500,blank=True, null=True)
    days_counter = models.CharField(max_length=500, blank=True, null=True)
    task_days = models.CharField(max_length=500, blank=True, null=True)
    exceed_days = models.CharField(max_length=500, blank=True, null=True)
    task_deadline = models.DateTimeField(null=True)
    report = models.FileField(upload_to='', null=True, blank=True)
    invoice = models.FileField(upload_to='', null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    case_inventory_found = models.CharField(max_length=255, default='Your Search is Found In Case Inventory Database')


    def __str__(self):
        return self.task_title

    def delete(self, *args, **kwargs):
        self.report.delete()
        self.invoice.delete()
        super().delete(*args, **kwargs)


class Moses(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    age = models.CharField(max_length=100,blank=True, null=True)
    gender = models.CharField(max_length=100,blank=True, null=True)



