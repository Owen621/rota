from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from main.decorators import manager_check, unauthenticated_user, authenticated_user
from .forms import CompanyForm, RegisterForm, AddEmployee, ExtendedUserForm
from .models import Employee
from django.contrib.auth import login, authenticate
import datetime


@unauthenticated_user
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        company_form = CompanyForm(response.POST)
        extended_form = ExtendedUserForm(response.POST)
        if (form.is_valid() and company_form.is_valid()) and extended_form.is_valid():
            user = form.save()
            
            extendedUserInstance = extended_form.save(commit=False)
            extendedUserInstance.account = "Manager"
            extendedUserInstance.user = user
            extendedUserInstance.save()
            companyInstance = company_form.save(commit=False)
            companyInstance.user = user
            companyInstance.save()
            return redirect("/login")
        else:
            pass
    else:
        form = RegisterForm()
        company_form = CompanyForm()
        extended_form = ExtendedUserForm()
    context = {'form' : form, 'company_form' : company_form, 'extended_form':extended_form}
    return render(response, "register/register.html", context)


@authenticated_user
@manager_check
def addemps(request):
    submitted = False
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        emp_form = AddEmployee(request.POST)
        extended_form = ExtendedUserForm(request.POST)
        if user_form.is_valid() and emp_form.is_valid() and extended_form.is_valid():
            
            userInstance = user_form.save()
            extendedUserInstance = extended_form.save(commit=False)
            extendedUserInstance.user = userInstance
            extendedUserInstance.account = "Employee"
            extendedUserInstance.save()
            employeeInstance = emp_form.save(commit=False)
            employeeInstance.manager = request.user
            employeeInstance.extended_user = extendedUserInstance
            employeeInstance.save()

    
            return redirect("/addemployees?submitted=True")
    else:
        user_form = RegisterForm(request.POST)
        emp_form = AddEmployee(request.POST)
        extended_form = ExtendedUserForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "main/addemployees.html", {"user_form":user_form,
    "emp_form":emp_form, 'submitted':submitted, 'extended_form':extended_form})

@unauthenticated_user
def loginPage(response):

    if response.method == "POST":
        username = response.POST.get('username')
        password = response.POST.get('password')

        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('/')

    return render(response, "registration/login.html")


@authenticated_user
@manager_check
def companyUpdate(response):

    if response.method == "POST":
        form = CompanyForm(response.POST, instance=response.user.company)
        if form.is_valid():
            form.save()
            return redirect("/company")
        else:
            pass
    else:
        form = CompanyForm(instance=response.user)
    company = response.user.company   


    return render(response, "main/company.html", {"form":form, "company":company})


@authenticated_user
@manager_check
def employeeInfo(response):

    company = response.user.company
    employees = Employee.objects.filter(manager=response.user.id)

    total = 0.0
    mon = 0.0
    tue = 0.0
    wed = 0.0
    thu = 0.0
    fri = 0.0
    sat= 0.0
    sun = 0.0

    for employee in employees:

        wage = employee.hourly_pay
        if employee.monday != " ":
            shift = employee.monday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)
            mon += (((difference.seconds)/60)/60)*wage

        if employee.tuesday != " ":
            shift = employee.tuesday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            tue += ((difference.seconds)/60)*wage

        if employee.wednesday != " ":
            shift = employee.wednesday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            wed += ((difference.seconds)/60)*wage

        if employee.thursday != " ":
            shift = employee.thursday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            thu += ((difference.seconds)/60)*wage

        if employee.friday != " ":
            shift = employee.friday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            fri += ((difference.seconds)/60)*wage

        if employee.saturday != " ":
            shift = employee.saturday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            sat += ((difference.seconds)/60)*wage
        
        if employee.sunday != " ":
            shift = employee.sunday.split("-")
            datetime1 = datetime.datetime.strptime(shift[0], '%H:%M')
            datetime2 = datetime.datetime.strptime(shift[1], '%H:%M')
            difference = (datetime2-datetime1)/60
            sun += ((difference.seconds)/60)*wage
        
        total = mon+tue+wed+thu+fri+sat+sun

    return render(response, "main/employeeinfo.html", {"employees":employees, "company": company, 
    "mon":mon, "tue":tue, "wed":wed, "thu":thu, "fri":fri, "sat":sat,
    "sun":sun, "total":total})
