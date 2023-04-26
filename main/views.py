
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.decorators import emp_check, manager_check, unauthenticated_user, authenticated_user
from register.models import Employee
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
import io


@authenticated_user
@emp_check
def rota(request):
    empuser = Employee.objects.get(extended_user_id=request.user.id)
    manager = User.objects.get(id=empuser.manager_id)
    company = manager.company
    employees = Employee.objects.filter(manager=manager)
    return render(request, "main/rota.html", {
        "employees": employees.all, "manager": manager, "company": company, "empuser":empuser})



@authenticated_user
@manager_check
def pdf_rota(request):

    employees = Employee.objects.filter(manager=request.user.id) 
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    textobject = c.beginText()
    textobject.setTextOrigin(200, 100)

    
   

    count = 1
    data= []
    for employee in reversed(employees):
        data.append([employee.first_name + " " + employee.last_name, employee.role,
        employee.monday, employee.tuesday, employee.wednesday, employee.thursday,
        employee.friday, employee.saturday, employee.sunday])
        count+=1

    data.append(["Name", "Role", "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"])
    table=Table(data,9*[0.72*inch], count*[0.72*inch])
    table.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTSIZE',(0,0),(-1,-1), 7),
    ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]))


    width = 1000
    height = 1000
    x,y = (20*mm, 20*mm)
    table.wrapOn(c, width, height)
    table.drawOn(c, x, y)
    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="Rota.pdf")


@unauthenticated_user
def welcome(response):
    return render(response, "main/welcome.html")


def empty(request):

    if request.user.is_authenticated:
        if request.user.extendeduser.account == "Manager":
            return redirect("/info")
        else:
            return redirect("/rota")
    else:
        return redirect("/welcome")

@authenticated_user
@manager_check
def info(response):
    return render(response, "main/info.html")

@authenticated_user
@manager_check
def generateRota(request):
    manager = User.objects.get(id=request.user.id)
    company = request.user.company
    none = False
    employees = Employee.objects.filter(manager=request.user.id)
    
    if len(employees) == 0:
        none = True
    
    publish = request.POST.get('publish', None)
    if publish == "published":
        publish = True
        company.companySave()
    generate = request.POST.get('generate', None)
    if generate == "generated":
        generate = True
        company.companyGenerated()




    dict = {"employees": employees.all, "manager": manager, "none": none, 
    "publish": publish, "generate": generate, "company": company}
    return render(request, "main/generate.html", dict)


@authenticated_user
@manager_check
def home(request):
    manager = User.objects.get(id=request.user.id)
    company = request.user.company
    none = False
    employees = Employee.objects.filter(manager=request.user.id)

    clear = request.POST.get('clear', None)
    if clear == "cleared":
        clear = True
        company.companyClear()

        for employee in employees:
            employee.unsave()

    if len(employees) == 0:
        none = True

    return render(request, "main/home.html", {
        "employees": employees.all, "manager": manager, 
        "none": none, "company": company, "clear": clear})


@authenticated_user
@manager_check
def customRota(request):
    manager = User.objects.get(id=request.user.id)
    company = request.user.company
    none = False
    employees = Employee.objects.filter(manager=request.user.id)

    if len(employees) == 0:
        none = True

    if 'edited' in request.GET:
        company.companySave()
    
    return render(request, "main/custom.html", {
        "employees": employees.all, "manager": manager, 
        "none": none, "company": company})


class editView(UpdateView):

    model = Employee
    template_name = 'main/edit.html'
    fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


    def get_success_url(self):
        return ('/custom?edited')


class updateInfo(UpdateView):

    model = Employee
    template_name = 'main/update.html'
    fields = ['first_name', 'last_name', 'birth_date', 'role', 'hours_per_week', 'hourly_pay']


    def get_success_url(self):
        return ('/employeeinfo?edited')

def deleteEmp(response, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except:
        redirect("/employeeinfo")
    if employee.manager != response.user:
        return redirect("/employeeinfo")
        
    deleteEmployee = response.POST.get('deleteEmployee', None)
    if deleteEmployee == "deleted":
        
        employee.extended_user.user.delete()
        employee.extended_user.delete()
        employee.delete()
        return redirect("/employeeinfo")
    
    else:
        return render(response, "main/deleteEmp.html", {
            "employee":employee, "deleteEmployee":deleteEmployee})