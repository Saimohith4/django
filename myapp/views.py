from django.shortcuts import render,redirect
from myapp.forms import Employeeform
from  myapp.models import Employee

# Create your views here.
def add(request):
    empform = Employeeform()
    if request.method == 'POST':
        empform = Employeeform(request.POST)
        if empform.is_valid():
            empform.save(commit=True)
            return redirect('emps')
    return render(request,'myapp/addemployee.html',{"form":empform})

def showemployees(request):
    emplist = Employee.objects.all()
    return render(request,'myapp/employees.html',{"employees":emplist})

def findemployee(request,id):

    employee = Employee.objects.get(id=id)

    return render(
        request,
        'myapp/findemployee.html',
        {'employee':employee}
    )

def deleteemployee(request,id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('emps')


def editemployee(request,id):

    employee = Employee.objects.get(id=id)

    form = Employeeform(instance=employee)

    if request.method == 'POST':

        form = Employeeform(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            return redirect('emps')

    return render(
        request,
        'myapp/addemployee.html',
        {'form':form}
    )