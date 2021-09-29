from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import os
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from rms.models import User


class Jumbe(models.Model):
    x = models.CharField(max_length=100,blank=True, null=True)
    y = models.CharField(max_length=100,blank=True, null=True)
    z = models.CharField(max_length=100,blank=True, null=True)

class Rusumo(models.Model):
    e = models.CharField(max_length=100,blank=True, null=True)
    f = models.CharField(max_length=100,blank=True, null=True)
    g = models.CharField(max_length=100,blank=True, null=True)


class Tela(models.Model):
    p = models.CharField(max_length=100,blank=True, null=True)
    q = models.CharField(max_length=100,blank=True, null=True)
    r = models.CharField(max_length=100,blank=True, null=True)
    

class Company(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    region = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    tel = models.CharField(max_length=500, null=True, blank=True)
    fax = models.CharField(max_length=500, null=True, blank=True)
    order_number = models.CharField(max_length=500, null=True, blank=True)
    show_avarage = models.CharField(max_length=500, null=True, blank=True)
    show_general = models.CharField(max_length=500, null=True, blank=True)
    display_package = models.CharField(max_length=500, null=True, blank=True)
    allow_excel = models.CharField(max_length=500, null=True, blank=True)
    allow_pdf = models.CharField(max_length=500, null=True, blank=True)
    days_to_basic = models.CharField(max_length=500, null=True, blank=True)
    days_to_extended = models.CharField(max_length=500, null=True, blank=True)
    display_biometric = models.CharField(max_length=500, null=True, blank=True)
    show_statistics = models.CharField(max_length=500, null=True, blank=True)
    allow_import = models.CharField(max_length=500, null=True, blank=True)
    idcheck = models.CharField(max_length=500, null=True, blank=True)
    emphistory = models.CharField(max_length=500, null=True, blank=True)
    gapanalysis = models.CharField(max_length=500, null=True, blank=True)
    academic = models.CharField(max_length=500, null=True, blank=True)
    professional = models.CharField(max_length=500, null=True, blank=True)
    cvanalysis = models.CharField(max_length=500, null=True, blank=True)
    criminal = models.CharField(max_length=500, null=True, blank=True)
    adverse = models.CharField(max_length=500, null=True, blank=True)
    complaince = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(null=True)


    def __str__(self):
        return self.name



class Employee(models.Model):
    name_found = models.CharField(max_length=255, default='Your Search is Found In KYE Database')
    firstname = models.CharField(max_length=500, null=True, blank=True)
    middlename = models.CharField(max_length=500, null=True, blank=True)
    lastname = models.CharField(max_length=500, null=True, blank=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=500, null=True, blank=True)
    motech = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self):
        return self.firstname

