from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        Gender=request.POST.get("gender")
        print(name,email,age,Gender)
        query=Student(name=name,email=email,age=int(age),gender=Gender)
        query.save()
        return redirect('/')
    return render(request,"index.html")


def updateData(request,id):

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        Gender=request.POST.get("gender")
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=Gender
        edit.age=age
        edit.save()
        return redirect("/")


    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)
def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    
    


def about(request):
    return render(request,"about.html")