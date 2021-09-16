from django.shortcuts import render, redirect
from .models import Employer, Departement
from .forms import Form_employer


# Create your views here.

# To create employee
def employers(request):
    if request.method == "POST":

        form = Form_employer(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemployers")
            except:
                pass
    else:
        form = Form_employer()
    return render(request, "index.html", {'form':form})

# To show employee details
def showemployers(request):
    employees = Employer.objects.all()
    return render(request, "main.html", {'employees':employees})

# To delete employee details
def deleteEmployers(request, pk):
    employee = Employer.objects.get(pk=pk)
    employee.delete()
    return redirect("/showemployers")

# To edit employee details
def editemployers(request, pk):
    employee = Employer.objects.get(pk=pk)
    return render(request, "edit.html", {'employee':employee})

# To update employee details
def updateEmployers(request, pk):
    employee = Employer.objects.get(pk=pk)
    form = Form_employer(request.POST, instance= employee)
    if form.is_valid():        
        form.save()
        return redirect("/showemployers")
    return render(request, "main.html", {'employee': employee})


