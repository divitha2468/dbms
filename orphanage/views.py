from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import logout,authenticate,login as auth_login #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
import pymysql
# import pyrebase
# from .pyrebase import initialize_app
# from Crypto.PublicKey import RSA
from django.db import connection

from.models import parent,donor,orphan,adoption,donation
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("orphanage:sample_view")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="orphanage/register.html", context={"register_form":form})

# def login(request):
#     return render(request,"login.html")
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request,template_name="orphanage/sample_view.html",context=None)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request,template_name="orphanage/login.html", context={"login_form":form})
# def sample_view(request):
#     return render(request,"sample_view.html")
def logout_request(request):
    logout(request)
    messages.info(request,"you have successfully loggedout")
    return redirect("orphanage:sample_view")
def submitform(request):
    return render(request,"submitform.html")
def parentform(request):
    return render(request,"parentform.html")

def adoptionform(request):
    parent_data = parent.objects.all()
    orphan_data=orphan.objects.all()
    context = {
        'parent_data': parent_data,
        'orphan_data':orphan_data
    }
    return render(request,"adoptionform.html", context)

def donationform(request):
    donor_data = donor.objects.all()
    context = {
        'donor_data': donor_data
    }
    print(id)
    return render(request,"donationform.html",context)
def orphanform(request):
    return render(request,"orphanform.html")

def donorform(request):
    return render(request,"donorform.html")

def sample_view(request):
    return render(request,template_name='orphanage/sample_view.html')

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
    return render(request, template_name='orphanage/submitform.html')
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
    return render(request, template_name='orphanage/submitform.html')


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
    data = donor.objects.all()
    cursor=connection.cursor()
    cursor.execute("INSERT INTO orphanage_donor(donorname,donor_phno,donor_email,address,city,state,country) VALUES ('" + str(request.POST.get('dname')) + "','"+str(request.POST.get('dphno'))+"','"+str(request.POST.get('demailid'))+"','"+str(request.POST.get('dadd'))+"','"+str(request.POST.get('city'))+"','"+str(request.POST.get('state'))+"','"+str(request.POST.get('country'))+"')")
    return render(request, template_view='orphanage/submitform.html')

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
    cursor.execute("INSERT INTO orphanage_adoption(parent_id,orphan_id,orphanname,date) VALUES ('"+str(request.POST.get('oname'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'orphanage/submitform.html')

def submit_donation(request,id):
    d = donation(
        donor_id=donor.objects.get(id=id),
        cash = request.POST['cash'],
        amount= request.POST['amount'],
        date= request.POST['date'], 
    )
    d.save()
    # cursor=connection.cursor()
    # query=cursor.execute("INSERT INTO orphanage_donation(donor_id,cash,amount,date) VALUES ("+str(request.donor.id)+",'"+str(request.POST.get('cash'))+"','"+str(request.POST.get('amount'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'orphanage/submitform.html')

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



