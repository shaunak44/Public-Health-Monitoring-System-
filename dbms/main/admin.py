from django.contrib import admin
from .models import *

# Register your models here.
class CitizenAdmin(admin.ModelAdmin):
    fields = ['aadhaar','name','gender','email_id', "contact_id", "address_id"]

class AddressForm(admin.ModelAdmin):
    fields = ['street','city','state']

class ContactForm(admin.ModelAdmin):
    fields = ['contact_number']

class HospitalForm(admin.ModelAdmin):
    fields = ['name', 'address_id', 'no_of_beds', 'type_hos', 'contact_id']

class GeneralHealthForm(admin.ModelAdmin):
    fields = ['aadhaar','last_checkup_date','spo2','temperature', 'pulse_rate']

class CoMorbidityForm(admin.ModelAdmin):
    fields = ['aadhaar','diabetes','hypertension','asthma']

class financial_status_form(admin.ModelAdmin):
    fields = ('pan_number','aadhaar','job_profile','annual_income', 'job_security')

class traits_form(admin.ModelAdmin):
    fields = ('aadhaar','age','weight','height', 'bmi')

class insurance_form(admin.ModelAdmin):
    fields = ('insurance_id','aadhaar','company_name','category')

class doctor_form(admin.ModelAdmin):
    fields = ('hospital_id','aadhaar','specialization')

class treatment_form(admin.ModelAdmin):
    fields = ('aadhaar','hospital_id', 'doctor_id', 'start_date', 'end_date')

class scheme_form(admin.ModelAdmin):
    fields = ('scheme_id','hospital_id', 'scheme_name')



admin.site.register(citizen, CitizenAdmin)
admin.site.register(address, AddressForm)
admin.site.register(contact, ContactForm)
admin.site.register(hospital, HospitalForm)
admin.site.register(general_health, GeneralHealthForm)
admin.site.register(co_morbidity, CoMorbidityForm)
admin.site.register(financial_status,   financial_status_form)
admin.site.register(traits, traits_form)
admin.site.register(insurance, insurance_form)
admin.site.register(doctor, doctor_form)
admin.site.register(treatment, treatment_form)
admin.site.register(scheme, scheme_form)