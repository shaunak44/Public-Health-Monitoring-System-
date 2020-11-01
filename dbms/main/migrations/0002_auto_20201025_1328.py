# Generated by Django 3.1.2 on 2020-10-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='co_morbidity',
            fields=[
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.citizen')),
                ('diabetes', models.BooleanField(default=False)),
                ('hypertension', models.BooleanField(default=False)),
                ('asthma', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.IntegerField(primary_key=True, serialize=False)),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='general_health',
            fields=[
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.citizen')),
                ('last_check_date', models.DateField()),
                ('spo2', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('pulse_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('hospital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('no_of_beds', models.IntegerField()),
                ('type_hos', models.CharField(max_length=20)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.address')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contact')),
            ],
        ),
        migrations.CreateModel(
            name='traits',
            fields=[
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.citizen')),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('bmi', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='citizen',
            old_name='aadhar',
            new_name='aadhaar',
        ),
        migrations.CreateModel(
            name='insurance',
            fields=[
                ('insurance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.citizen')),
            ],
        ),
        migrations.CreateModel(
            name='financial_status',
            fields=[
                ('pan_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('job_profile', models.CharField(max_length=20)),
                ('annual_income', models.IntegerField()),
                ('job_security', models.BooleanField()),
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.citizen')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=20)),
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.citizen')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
        ),
        migrations.AlterField(
            model_name='citizen',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.address'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='contact_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contact'),
        ),
        migrations.CreateModel(
            name='treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.citizen')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
            options={
                'unique_together': {('aadhaar', 'hospital_id', 'doctor_id')},
            },
        ),
        migrations.CreateModel(
            name='scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_id', models.IntegerField()),
                ('scheme_name', models.CharField(max_length=50)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
            options={
                'unique_together': {('scheme_id', 'hospital_id')},
            },
        ),
    ]