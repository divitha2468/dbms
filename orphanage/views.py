from django.shortcuts import render
import pymysql
 
from django.db import connection


from.models import parent,adoption,donation
def parentform(request):
    return render(request,"parentform.html")
def adoptionform(request):
    return render(request,"adoptionform.html")
def donationform(request):
    return render(request,"donationform.html")

def sample_view(request):
    return render(request,'sample_view.html')

def submit_parent(request):
    
    p = parent(
        firstname = request.POST['fname'],
        lastname = request.POST['lname'],
        email = request.POST['emailid'],   
        phno= request.POST['phno'], 
        gender= request.POST['gender'], 
        address= request.POST['add'], 
        city= request.POST['city'], 
        pincode= request.POST['pincode'], 
        state= request.POST['state'], 
        country= request.POST['country'],
        

    )
    
    p.save()
    return render(request, 'submitform.html')
def submit_adoption(request):
    
    a = adoption(
        parentfname = request.POST['pfname'],
        parentlname = request.POST['plname'],
        phno= request.POST['phno'],
        email = request.POST['emailid'],     
        address= request.POST['add'], 
        orphanname= request.POST['oname'], 
        orphanid= request.POST['oid'], 
        date= request.POST['date'], 
    
    )
    
    a.save()
    return render(request, 'sample_view.html',message="done")
def submit_donation(request):
    
    d = donation(
        donor_id = request.POST['did'],
        cash = request.POST['cash'],
        amount= request.POST['amount'],
        date= request.POST['date'], 
    
    )
    
    d.save()
    return render(request, 'submitform.html')
def view_parent(request):
        query=parent.objects.raw("select * from parent")
        print(query)
        return render(request,'view_parent.html',{'query':query})

    