from django.shortcuts import render, redirect
from django.urls import path, include
from django.http import HttpResponse
from .models import citizen, address
from .forms import *
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def index1(response):
    return render(response, "main/home.html", {})

def create(response):
    form = UserForm()
    if(response.method == "POST"):
        print(response.POST)
    return render(response, "main/create.html", {"form":form})

def options(response):
    if(response.user.is_authenticated):
        return render(response, "main/options.html", {})
    else:
        messages.info(response, "Please Login First!")
        return redirect('login')

def wrong(response):
    return render(response, "main/wrong.html", {})

def citizenFunction(request):
    if(request.user.is_authenticated):
        print(request.POST)
        cform = citizen_form(request.POST)
        aform = address_form(request.POST)
        conform = contact_form(request.POST)
        if(aform.is_valid()):
            t_add = aform.save()
        if(conform.is_valid()):
            t_con = conform.save()

        if(cform.is_valid()):
            try:
                t_citi = cform.save(commit=False)
                t_citi.address_id = t_add
                t_citi.contact_id = t_con
                request.session['aadhaar_number'] = t_citi.aadhaar
                t_citi.save()
                return redirect('citizen1')
            except Exception as e:
                print(e)

        form = citizen_form()
        form7 = contact_form()
        form8 = address_form()

        return render(request, "main/citizen.html", {"form": form, "form7": form7,"form8": form8})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')

def doctorFunction(request):
    if(request.user.is_authenticated):
        print(request.POST)
        cform = citizen_form(request.POST)
        aform = address_form(request.POST)
        conform = contact_form(request.POST)
        if(aform.is_valid()):
            t_add = aform.save()
        if(conform.is_valid()):
            t_con = conform.save()

        if(cform.is_valid()):
            try:
                t_citi = cform.save(commit=False)
                t_citi.address_id = t_add
                t_citi.contact_id = t_con
                request.session['aadhaar_number'] = t_citi.aadhaar
                t_citi.save()
                return redirect('doctor1')
            except Exception as e:
                print(e)

        form = citizen_form()
        form7 = contact_form()
        form8 = address_form()

        return render(request, "main/citizen.html", {"form": form, "form7": form7,"form8": form8})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')


def citizen1(request):
    if(request.user.is_authenticated):
        tform = traits_form(request.POST)

        if(tform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_trait = tform.save(commit=False)
            try:
                t_trait.aadhaar = temp_citi
                temp = (10000*int(request.POST.get('weight'))/int(request.POST.get('weight'))**2)
                setattr(t_trait, "bmi", temp)
            except Exception as e:
                print(e)
            t_trait.save()



        genform = general_health_form(request.POST)

        if(genform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_gen = genform.save(commit=False)
            try:
                t_gen.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_gen.save()


        insform = insurance_form(request.POST)

        if(insform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_ins = insform.save(commit=False)
            try:
                t_ins.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_ins.save()



        coform = co_morbidity_form(request.POST)

        if(coform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_co = coform.save(commit=False)
            try:
                t_co.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_co.save()


        finform = financial_status_form(request.POST)

        if(finform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_fin = finform.save(commit=False)
            try:
                t_fin.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_fin.save()
            return redirect('confirmation')

        form1 = traits_form()
        form2 = treatment_form()
        form3 = general_health_form()
        form4 = co_morbidity_form()
        form5 = financial_status_form()
        form6 = insurance_form()
        return render(request, "main/citizen1.html", {"form1": form1, "form2": form2,"form3": form3,"form4": form4,
                                                    "form5": form5,"form6": form6})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')

def doctor1(request):
    
    if(request.user.is_authenticated):
        tform = traits_form(request.POST)
        if(tform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_trait = tform.save(commit=False)
            try:
                t_trait.aadhaar = temp_citi
                temp = (10000*int(request.POST.get('weight'))/int(request.POST.get('weight'))**2)
                setattr(t_trait, "bmi", temp)
            except Exception as e:
                print(e)
            t_trait.save()
        genform = general_health_form(request.POST)
        if(genform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_gen = genform.save(commit=False)
            try:
                t_gen.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_gen.save()
        insform = insurance_form(request.POST)
        if(insform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_ins = insform.save(commit=False)
            try:
                t_ins.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_ins.save()
        coform = co_morbidity_form(request.POST)
        if(coform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_co = coform.save(commit=False)
            try:
                t_co.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_co.save()
        finform = financial_status_form(request.POST)
        if(finform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_fin = finform.save(commit=False)
            try:
                t_fin.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_fin.save()

        docform = doctor_form(request.POST)
        if(docform.is_valid()):
            temp_citi = citizen.objects.get(aadhaar=request.session.get('aadhaar_number'))
            t_doc = docform.save(commit=False)
            try:
                t_doc.aadhaar = temp_citi    
            except Exception as e:
                print(e)
            t_doc.save()
            return redirect('confirmation')


        form1 = traits_form()
        form2 = treatment_form()
        form3 = general_health_form()
        form4 = co_morbidity_form()
        form5 = financial_status_form()
        form6 = insurance_form()
        form7 = doctor_form()
        return render(request, "main/doctor1.html", {"form1": form1, "form2": form2,"form3": form3,"form4": form4,
                                                        "form5": form5,"form6": form6, "form7":form7}) 
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')

def hospitalFunction(request):
    if(request.user.is_authenticated):
        return render(request, 'main/Hos_options.html', {})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')
def hospital1(request):
    if(request.user.is_authenticated):
        print(request.POST)
        hform = hospital_form(request.POST)
        aform = address_form(request.POST)
        conform = contact_form(request.POST)
        if(aform.is_valid()):
            t_add = aform.save()
        if(conform.is_valid()):
            t_con = conform.save()

        if(hform.is_valid()):
            try:
                t_hos = hform.save(commit=False)
                t_hos.address_id = t_add
                t_hos.contact_id = t_con
                #request.session['aadhaar_number'] = t_citi.aadhaar
                t_hos.save()
                return redirect('confirmation')
            except Exception as e:
                print(e)

        form = hospital_form()
        form7 = contact_form()
        form8 = address_form()

        return render(request, "main/hospital1.html", {"form": form, "form7": form7,"form8": form8})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')
def hospital2(request):
    if(request.user.is_authenticated):
        tform = treatment_form(request.POST)
        sform = scheme_form(request.POST)
        if(tform.is_valid()):
            t_treat = tform.save()

        if(sform.is_valid()):
            t_scheme = sform.save(commit=False)
            t_hos = hospital.objects.get(hospital_id=request.POST.get('hospital_id'))
            t_scheme.hospital_id = t_hos
            t_scheme.save()
            return redirect('confirmation')
    
        form = treatment_form()
        form1 = scheme_form()
        return render(request, "main/hospital2.html", {"form":form, "form1":form1})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')

def confirmation(request):
    if(request.user.is_authenticated):
        return render(request, "main/confirmation.html", {})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')

'''def doctorFun(response):
    return render(response, "main/doctor.html", {})'''

def profileFunction(request):
    if(request.user.is_authenticated):
        if(request.method == "POST"):
            #print(request.POST)
            if(len(request.POST.get('aadhaar')) == 12):
                aadhaarid = request.POST.get('aadhaar') 
                citizenData = citizen.objects.get(aadhaar = aadhaarid)
                addressData = address.objects.get(address_id = int(str(citizenData.address_id)))
                try:
                    treatmentData = treatment.objects.get(aadhaar = aadhaarid)
                except:
                    treatmentData = None
                try:
                    doctorData = doctor.objects.get(aadhaar = aadhaarid)
                except Exception as e:
                    print(e)
                    doctorData = None
                contactData = contact.objects.get(contact_id = int(str(citizenData.contact_id)))
                traitsData = traits.objects.get(aadhaar = aadhaarid)
                general_healthData = general_health.objects.get(aadhaar = aadhaarid)
                co_morbidityData = co_morbidity.objects.get(aadhaar = aadhaarid)
                financial_statusData = financial_status.objects.get(aadhaar = aadhaarid)
                insuranceData = insurance.objects.get(aadhaar = aadhaarid)
                
                return render(request, 'main/aadhaarData.html', {"citizenData":citizenData, "financial_statusData":financial_statusData, 
                                "addressData":addressData, "contactData":contactData, "traitsData":traitsData, "general_healthData":general_healthData
                                , "co_morbidityData":co_morbidityData, "insuranceData":insuranceData, "treatmentData":treatmentData, "doctorData":doctorData})
            else:
                hospitalid = request.POST.get('aid')
        form = citizen_form()
        return render(request, 'main/profile.html', {"form":form})
    else:
        messages.info(request, "Please Login First!")
        return redirect('login')
def test(request):
    return render(request, 'main/index.html', {})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("index") #add view name here

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

def login_request(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request=request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password, type(username), type(password),"*****")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('options')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('wrong')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('wrong')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def stats(request):
    labels = ['Having job security', 'Not having job security']
    data = []
    data.append(financial_status.objects.filter(job_security=True).count())
    data.append(financial_status.objects.filter(job_security=False).count())

    labels_d = ['Diabetes', 'Hypertension', 'Asthma']
    data_d = []
    data_d.append(co_morbidity.objects.filter(diabetes=True).count())
    data_d.append(co_morbidity.objects.filter(hypertension=True).count())
    data_d.append(co_morbidity.objects.filter(asthma=True).count())

    labels_doc = ['Non-Doctors', 'Doctors']
    data_doc = []
    data_doc.append(citizen.objects.filter().count() - doctor.objects.filter().count())
    data_doc.append(doctor.objects.filter().count())

    labels_age = ['0-20 years', '21-58 years', 'Above 58']
    data_age = []
    data_age.append(traits.objects.filter(age__lte = 20).count())
    data_age.append(traits.objects.filter(age__lte = 58).count() - traits.objects.filter(age__lte = 20).count())
    data_age.append(traits.objects.filter(age__gte = 59).count())
    
    return render(request, 'main/stats.html', {
        'labels': labels,
        'data': data,
        'labels_d': labels_d,
        'data_d': data_d,
        "labels_doc":labels_doc,
        "data_doc":data_doc,
        "labels_age":labels_age,
        "data_age":data_age,
    })