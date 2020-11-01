from django import forms
from main.models import *
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class citizen_form(forms.ModelForm):
    class Meta():
        model = citizen
        fields = ('aadhaar','name','gender','email_id')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-group mb-3'}),
        }

class address_form(forms.ModelForm):
    class Meta():
        model = address
        fields = ('street','city','state')

class hospital_form(forms.ModelForm):
    class Meta():
        model = hospital
        fields = ('hospital_id','name','no_of_beds', 'type_hos')

class contact_form(forms.ModelForm):
    class Meta():
        model = contact
        fields = ('contact_number',)

class general_health_form(forms.ModelForm):
    class Meta():
        model = general_health
        fields = ('last_checkup_date','spo2','temperature', 'pulse_rate')

class co_morbidity_form(forms.ModelForm):
    class Meta():
        model = co_morbidity
        fields = ('diabetes','hypertension','asthma')

class financial_status_form(forms.ModelForm):
    class Meta():
        model = financial_status
        fields = ('pan_number','job_profile','annual_income', 'job_security')

class traits_form(forms.ModelForm):
    class Meta():
        model = traits
        fields = ('age','weight','height', 'bmi')

class insurance_form(forms.ModelForm):
    class Meta():
        model = insurance
        fields = ('insurance_id','company_name','category')

class doctor_form(forms.ModelForm):
    class Meta():
        model = doctor
        fields = ('doctor_id','hospital_id','specialization')

class treatment_form(forms.ModelForm):
    class Meta():
        model = treatment
        fields = ('hospital_id', 'doctor_id', 'aadhaar', 'start_date', 'end_date')

class scheme_form(forms.ModelForm):
    class Meta():
        model = scheme
        fields = ('scheme_id','scheme_name')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': 'Same as your Aadhaar No.',
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
