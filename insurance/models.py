from django.db import models
import os
from django.conf import settings
from rms.models import User


class Insurancefile(models.Model):
    file_no = models.CharField(max_length=500, null=True, blank=True)
    insurer = models.CharField(max_length=500, null=True, blank=True)
    claimant = models.CharField(max_length=500, null=True, blank=True)
    driver = models.CharField(max_length=500, null=True, blank=True)
    deceased = models.CharField(max_length=500, null=True, blank=True)
    insurance_found = models.CharField(max_length=255, default='Your Search is Found In Insurance Database')


    def __str__(self):
        return self.insurer

