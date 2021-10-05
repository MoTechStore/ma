from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.conf import settings




class Myfile(models.Model):
    myfile = models.FileField(upload_to='')
    entity = models.CharField(max_length=1000)

    def __str__(self):
        return self.entity

    def delete(self, *args, **kwargs):
        self.myfile.delete()
        self.entity.delete()
        super().delete(*args, **kwargs)



class Files(models.Model):
    myfile = models.FileField(upload_to='report/')
    entity = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.myfile

    def delete(self, *args, **kwargs):
        self.myfile.delete()
        super().delete(*args, **kwargs)


class User(AbstractUser):
    is_cis_officer = models.BooleanField(default=False)
    is_rms_officer = models.BooleanField(default=False)
    is_cis_admin = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class File(models.Model):
    file_name = models.CharField(max_length=1000)
    file_number = models.CharField(max_length=1000)
    cupboard_name = models.CharField(max_length=1000)
    cupboard_number = models.CharField(max_length=1000)
    shelve_number = models.CharField(max_length=1000)
    about_file = models.CharField(max_length=1000)
    current_owner = models.CharField(max_length=1000, null=True, blank=True)
    ref_number = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    file_found = models.CharField(max_length=255, default='Your Search is Found In Archiving Database')




class Store(models.Model):
    document_name = models.CharField(max_length=1000)
    document_number = models.CharField(max_length=1000)
    file_name = models.CharField(max_length=1000)
    file_number = models.CharField(max_length=1000)
    cupboard_name = models.CharField(max_length=1000)
    cupboard_number = models.CharField(max_length=1000)
    shelve_number = models.CharField(max_length=1000)
    about_document = models.CharField(max_length=1000)
    current_owner = models.CharField(max_length=1000, null=True, blank=True)
    ref_number = models.CharField(max_length=1000)
    name_list = models.CharField(max_length=1000)
    accessed_no = models.IntegerField(null=True, blank=True)
    file = models.FileField(upload_to='', null=True, blank=True)
    

class Letter(models.Model):
    sender = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    ref_number = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(blank=True, null=True)
    iletter_found = models.CharField(max_length=255, default='Your Search is Found In Incoming Letters')



class Letters(models.Model):
    sender_name = models.CharField(max_length=1000)
    receiver_address = models.CharField(max_length=1000)
    receiver_name = models.CharField(max_length=1000)
    contact_two = models.CharField(max_length=1000)
    desc_two = models.CharField(max_length=1000)
    ref_number_two = models.CharField(max_length=1000, null=True)
    date_two = models.DateTimeField(blank=True, null=True)
    oletter_found = models.CharField(max_length=255, default='Your Search is Found In Outgoing Letters')
