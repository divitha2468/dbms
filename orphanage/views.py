from django.shortcuts import render
import pymysql
 
from django.db import connection

cursor=connection.cursor()
from.models import parent,adoption
def parentform(request):
    return render(request,"parentform.html")

def sample_view(request):
    return render(request,'sample_view.html')

def submit_form(request):
    # cursor.execute("INSERT INTO orphanage_parent(firstname,lastname,email,phno,gender,address,city,pincode,state,country) VALUES ('" + request.POST.get('fname') + "','"+request.POST.get('lname')+"','"+request.POST.get('emailid')+"','"+request.POST.get('phno')+"','"+request.POST.get('gender')+"' ,'"+request.POST.get('address')+"','"+request.POST.get('city')+"','"+str(request.POST.get('pincode'))+"','"+request.POST.get('state')+"','"+request.POST.get('country')+"')")
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
    return render(request, 'adoptionform.html')
def adoption_form(request):
    a = adoption(
        parentname = request.POST['pname'],
        phno= request.POST['phno'],
        email = request.POST['emailid'],     
        address= request.POST['add'], 
        orphanname= request.POST['oname'], 
        orphanid= request.POST['oid'], 
        date= request.POST['date'], 
    
    )
    a.save()
    return render(request, 'sample_view.html')