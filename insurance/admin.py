from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from insurance.models import Insurancefile

@admin.register(Insurancefile)
class InsuranceAdmin(ImportExportModelAdmin):
    pass