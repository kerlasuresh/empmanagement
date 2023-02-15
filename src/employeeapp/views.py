from django.shortcuts import render
from .models import EmployeeData
import faker
fake=faker.Faker()
from django.http import HttpResponse
from django.db.models import Q
def EmployeeView(request):
    for i in range(20):
        EmployeeData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        salary=fake.random_element(elements = (15000,20000,25000,30000,35000,40000)),
        job=fake.random_element(elements = ('software','Triner','Marketing','Sales','Security','Hardware')),
        company=fake.random_element(elements = ('TCS','Wipro','Infosys','IBM','TechMahindra')),
        location=fake.random_element(elements = ('HYD','Bang','Chennai','Pune'))
        ).save()
    return HttpResponse("Data Saved Successfully")

def homepage(request):
    data=EmployeeData.objects.all()
    return render(request,'homepage.html',{'data':data})

def mainView(request):
    return render(request,'mainpage.html')

def hyddata(request):
    if request.method=='GET':
        hyddata=EmployeeData.objects.filter(location='HYD')
        return render(request,'hyddata.html',{'hyddata':hyddata})
    else:
        companyName=request.POST.get('companyName')
        hyddata=EmployeeData.objects.filter(Q(location =  'HYD') & Q(company=companyName))
        return render(request,'hyddata.html',{'hyddata':hyddata})

def bangdata(request):
    if request.method=='GET':
        bangdata=EmployeeData.objects.filter(location='Bang')
        return render(request,'bangdata.html',{'bangdata':bangdata})
    else:
        companyName=request.POST.get('companyName')
        bangdata=EmployeeData.objects.filter(Q(location =  'Bang') & Q(company=companyName))
        return render(request,'bangdata.html',{'bangdata':bangdata})

def chennaidata(request):
    if request.method=='GET':
        chennaidata=EmployeeData.objects.filter(location='Chennai')
        return render(request,'chennai.html',{'chennaidata':chennaidata})
    else:
        companyName=request.POST.get('companyName')
        chennaidata=EmployeeData.objects.filter(Q(location =  'Chennai') & Q(company=companyName))
        return render(request,'chennai.html',{'chennaidata':chennaidata})
def punedata(request):
    if request.method=='GET':
        punedata=EmployeeData.objects.filter(location='Pune')
        return render(request,'punedata.html',{'punedata':punedata})
    else:
        companyName=request.POST.get('companyName')
        punedata=EmployeeData.objects.filter(Q(location =  'Pune') & Q(company=companyName))
        return render(request,'punedata.html',{'punedata':punedata})
