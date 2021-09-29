from django import forms
from django.db import transaction
from django.forms.utils import ValidationError
from rms.models import Store
from .models import Store
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.contrib.auth.models import User






class CustomerForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['document_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['document_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['file_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['file_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['current_owner'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cupboard_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cupboard_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['shelve_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['about_document'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['ref_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['name_list'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
    class Meta:
        model = Store
        fields = ('document_name', 'current_owner', 'document_number', 'file_name', 'file_number', 'cupboard_number', 'cupboard_name', 'shelve_number', 'about_document', 'ref_number', 'name_list')



class UserForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control col-md-6'
        }


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


