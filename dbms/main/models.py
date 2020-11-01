from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class citizen(models.Model):
    gender_choice = [('M', 'Male'), ('F', 'Female')]
    aadhaar = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=gender_choice)
    address_id = models.ForeignKey("address", on_delete=models.CASCADE, default=None)
    contact_id = models.ForeignKey("contact", on_delete=models.CASCADE, default=None)
    email_id = models.CharField(max_length=20)
    def __str__(self):
        return u'{0}'.format(self.aadhaar)

class address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    def __str__(self):
        return u'{0}'.format(self.address_id)

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_number = models.CharField(max_length=10)
    def __str__(self):
        return u'{0}'.format(self.contact_id)

class traits(models.Model):
    aadhaar = models.OneToOneField("citizen", on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    bmi = models.FloatField()

class general_health(models.Model):
    aadhaar = models.OneToOneField("citizen", on_delete=models.CASCADE, primary_key=True)
    last_checkup_date = models.DateField()
    spo2 = models.IntegerField()
    temperature = models.FloatField()
    pulse_rate = models.IntegerField()

class co_morbidity(models.Model):
    aadhaar = models.OneToOneField("citizen", on_delete=models.CASCADE, primary_key=True)
    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)

class financial_status(models.Model):
    pan_number = models.CharField(max_length=10, primary_key=True)
    aadhaar = models.ForeignKey("citizen", on_delete=models.CASCADE)
    job_profile = models.CharField(max_length=20)
    annual_income = models.IntegerField()
    job_security = models.BooleanField()

class insurance(models.Model):
    insurance_id = models.IntegerField(primary_key=True)
    aadhaar = models.ForeignKey("citizen", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    hospital_id = models.ForeignKey("hospital", on_delete=models.CASCADE)
    aadhaar = models.ForeignKey("citizen", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=20)
    def __str__(self):
        return u'{0}'.format(self.doctor_id)

class hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address_id = models.ForeignKey("address", on_delete=models.CASCADE)
    no_of_beds = models.IntegerField()
    type_hos = models.CharField(max_length=20)
    contact_id = models.ForeignKey("contact", on_delete=models.CASCADE)
    def __str__(self):
        return u'{0}'.format(self.hospital_id)

class treatment(models.Model):
    class Meta:
        unique_together = (("aadhaar", 'hospital_id', 'doctor_id'), )
    aadhaar = models.ForeignKey("citizen", on_delete=models.CASCADE)
    hospital_id = models.ForeignKey("hospital", on_delete=models.CASCADE)
    doctor_id = models.ForeignKey("doctor", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    

class scheme(models.Model):
    class Meta:
        unique_together = (('scheme_id', 'hospital_id'), )
    scheme_id = models.IntegerField()
    hospital_id = models.ForeignKey("hospital", on_delete=models.CASCADE)
    scheme_name = models.CharField(max_length=50)






