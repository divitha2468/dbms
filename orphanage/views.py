from django.shortcuts import render
import pymysql
# import pyrebase
# from .pyrebase import initialize_app
# from Crypto.PublicKey import RSA
from django.db import connection

from.models import parent,donor,orphan,adoption,donation
  
def login(request):
    return render(request,"login.html")
def submit_login(request):
    return render(request,"sample_view.html")
def parentform(request):
    return render(request,"parentform.html")

def adoptionform(request):
    return render(request,"adoptionform.html")

def donationform(request):
    return render(request,"donationform.html")
def orphanform(request):
    return render(request,"orphanform.html")

def donorform(request):
    return render(request,"donorform.html")

def sample_view(request):
    return render(request,'sample_view.html')

def submit_parent(request):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO orphanage_parent(firstname,lastname,email,phno,gender,address,city,pincode,state,country) VALUES ('"+ str(request.POST.get('fname')) + "','"+str(request.POST.get('lname'))+"','"+str(request.POST.get('emailid'))+"','"+str(request.POST.get('phno'))+"','"+str(request.POST.get('gender'))+"' ,'"+str(request.POST.get('address'))+"','"+str(request.POST.get('city'))+"','"+str(request.POST.get('pincode'))+"','"+str(request.POST.get('state'))+"','"+str(request.POST.get('country'))+"')")
    # p = parent(
    #     parentid=request.POST['pid'],
    #     firstname = request.POST['fname'],
    #     lastname = request.POST['lname'],
    #     email = request.POST['emailid'],   
    #     phno= request.POST['phno'], 
    #     gender= request.POST['gender'], 
    #     address= request.POST['add'], 
    #     city= request.POST['city'], 
    #     pincode= request.POST['pincode'], 
    #     state= request.POST['state'], 
    #     country= request.POST['country'],
    # )
    # p.save()
    return render(request, 'submitform.html')
def submit_orphan(request):
    # o = orphan(
    #     orphanid= request.POST['oid'], 
    #     orphanname = request.POST['oname'],
    #     age = request.POST['age'],
    #     gender= request.POST['gender'], 
    #     dateofbirth= request.POST['dob'],
        
    # )
    # o.save()

    cursor=connection.cursor()
    query=cursor.execute("INSERT INTO orphanage_orphan(orphanname,gender,dateofbirth) VALUES ('" +str(request.POST.get('oname'))+"','"+str(request.POST.get('gender'))+"' ,'"+str(request.POST.get('dob'))+"')")
    return render(request, 'submitform.html')


def submit_donor(request):
    # d = donor(
    #     donorid = request.POST['did'],
    #     donorname = request.POST['dname'],
    #     donor_phno= request.POST['dphno'],
    #     donor_email = request.POST['demailid'],     
    #     address= request.POST['dadd'], 
    #     city= request.POST['city'], 
    #     state= request.POST['state'], 
    #     country= request.POST['country'],
    
    # )
    # d.save()
    cursor=connection.cursor()
    cursor.execute("INSERT INTO orphanage_donor(donorname,donor_phno,donor_email,address,city,state,country) VALUES ('" + str(request.POST.get('dname')) + "','"+str(request.POST.get('dphno'))+"','"+str(request.POST.get('demailid'))+"','"+str(request.POST.get('dadd'))+"','"+str(request.POST.get('city'))+"','"+str(request.POST.get('state'))+"','"+str(request.POST.get('country'))+"')")
    return render(request, 'submitform.html')

def submit_adoption(request):
    # a = adoption(
    #     parentid=request.POST['pid'],
    #     parentfname = request.POST['pfname'],
    #     parentlname = request.POST['plname'],
    #     phno= request.POST['phno'],
    #     email = request.POST['emailid'],     
    #     address= request.POST['add'], 
    #     orphanname= request.POST['oname'], 
    #     orphanid= request.POST['oid'], 
    #     date= request.POST['date'], 
    # )
    # a.save()
    cursor=connection.cursor()
    cursor.execute("INSERT INTO orphanage_adoption(parent,orphan,orphanname,date) VALUES ('" + str(request.POST.get('pid')) + "','"+str(request.POST.get('oid'))+"','"+str(request.POST.get('oname'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'submitform.html')

def submit_donation(request):
    # d = donation(
    #     donorid = request.POST['did'],
    #     cash = request.POST['cash'],
    #     amount= request.POST['amount'],
    #     date= request.POST['date'], 
    # )
    # d.save()
    cursor=connection.cursor()
    query=cursor.execute("INSERT INTO orphanage_donation(donor,cash,amount,date) VALUES ('" + str(request.POST.get('did')) + "','"+str(request.POST.get('cash'))+"','"+str(request.POST.get('amount'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'submitform.html')

def view_parent(request):
        data = parent.objects.all()
        return render(request,'view_parent.html',{'messages':data})
       
def view_orphan(request):
    data = orphan.objects.all()
    return render (request, 'view_orphan.html', {'msg':data})


def view_donor(request):
    data = donor.objects.all()
    return render  (request, 'view_donor.html', {'any':data})


def view_donationhistory(request):
    data = donation.objects.all()
    return render (request, 'view_donationhistory.html', {'his':data})


def view_adoptionhistory(request):
    data = adoption.objects.all()
    return render (request, 'view_adoptionhistory.html', {'adop':data}) 



