from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientForm(admin.ModelAdmin):
    list_display="name","phone","email","date","time","address"

admin.site.register(Patient,PatientForm)