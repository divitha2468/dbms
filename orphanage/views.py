from django.shortcuts import render
from django.shortcuts import redirect
# from .forms import NewUserForm
from django.contrib.auth import logout,authenticate,login as auth_login#add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
import pymysql
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# import pyrebase
# from .pyrebase import initialize_app
# from Crypto.PublicKey import RSA
from django.db import connection

from.models import staff,donor,orphan,adoption,donation
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             auth_login(request,user)
#             return redirect('orphanage:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'orphanage/register.html', {'form': form})  
# def login(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				auth_login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return render(request,template_name="orphanage/sample_view.html",context=None)
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request,template_name="orphanage/login.html", context={"login_form":form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('orphanage:sample_view')
    else:
        form = AuthenticationForm()
    return render(request, 'orphanage/login.html', {'form': form})
def sample_view(request):
    return render(request,"sample_view.html")
def deletestaff(request):
    staff_data=staff.objects.filter(deleted=0)
    context = {
        
        'staff_data':staff_data
    }
    return render(request,"deletestaff.html", context)
def logout_request(request):
    logout(request)
    messages.info(request,"you have successfully loggedout")
    return redirect("orphanage:sample_view")
def submitform(request):
    return render(request,"submitform.html")
def parentform(request):
    return render(request,"parentform.html")

def adoptionform(request):
    donor_data = donor.objects.all()
    orphan_data=orphan.objects.filter(adopted=0)
    context = {
        'donor_data': donor_data,
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
    staff_data = staff.objects.all()
    context = {
        'staff_data': staff_data
    }
    return render(request,"orphanform.html",context)

def donorform(request):
    return render(request,"donorform.html")
def sample_view(request):
    return render(request,'orphanage/sample_view.html')

# def submit_delete(request):
#     # deleted=request.GET['deleted']
#     # data=staff.objects.get(id=request.GET['id'])
#     # if data.deleted==0:
#     #     data.deleted=1
#     #     data.save(['deleted'])
#     staff_id=request.GET['id']
#     staff.objects.get(id=staff_id).update(deleted="1")
#     return render(request,'orphanage/submitform.html')
def submit_parent(request):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO orphanage_staff(staffname,email,phno,designation,pincode) VALUES ('"+ str(request.POST.get('sname')) + "', ' "+str(request.POST.get('emailid'))+"','"+str(request.POST.get('phno'))+"','"+str(request.POST.get('desig'))+"' ,'"+str(request.POST.get('pincode'))+"')")
    cursor.execute("INSERT INTO orphanage_sdetails(pincode,h_no,city,state,country) VALUES ('"+str(request.POST.get('pincode'))+"' ,'"+str(request.POST.get('h_no'))+"','"+str(request.POST.get('city'))+"','"+str(request.POST.get('state'))+"','"+str(request.POST.get('country'))+"')")
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
    return render(request,'orphanage/submitform.html')
def submit_orphan(request):
    o = orphan(
        staff_id= request.POST['id'], 
        orphanname = request.POST['oname'],
        # age = request.POST['age'],
        gender= request.POST['gender'], 
        dateofbirth= request.POST['dob'],
       
        
    )
    o.save()
    
    # cursor=connection.cursor()
    # query=cursor.execute("INSERT INTO orphanage_orphan(staffname,orphanname,gender,adopted,dateofbirth) VALUES ('" +str(request.POST.get('oname'))+"','" +str(request.POST.get('oname'))+"','"+str(request.POST.get('gender'))+"' ,'" +str(request.POST.get('adopted'))+"','"+str(request.POST.get('dob'))+"')")
    return render(request,'orphanage/submitform.html')


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
    cursor.execute("INSERT INTO orphanage_donor(donorname,email,phno,pincode) VALUES ('"+ str(request.POST.get('dname')) + "','"+str(request.POST.get('demailid'))+"','"+str(request.POST.get('dphno'))+"','"+str(request.POST.get('pincode'))+"')")
    cursor.execute("INSERT INTO orphanage_ddetails(pincode,h_no,city,state,country) VALUES ('"+str(request.POST.get('pincode'))+"' ,'"+str(request.POST.get('h_no'))+"','"+str(request.POST.get('city'))+"','"+str(request.POST.get('state'))+"','"+str(request.POST.get('country'))+"')")
    return render(request,"orphanage/submitform.html")

def submit_adoption(request):
    print(request.POST)
    a = adoption(
        donor=donor.objects.get(id=request.POST['donor_id']),
        orphan=orphan.objects.get(id=request.POST['orphan_id']),
        date= request.POST['date'], 
    )
    a.save()
    # cursor=connection.cursor()
    # cursor.execute("INSERT INTO orphanage_adoption(parent_id,orphan_id,orphanname,date) VALUES ('"+str(request.POST.get('oname'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'orphanage/submitform.html')

def submit_donation(request):
    d = donation(
        donor_id=request.POST['id'],
        cash = request.POST['cash'],
        kind = request.POST['kind'],
        date= request.POST['date'], 
    )
    d.save()
    # cursor=connection.cursor()
    # query=cursor.execute("INSERT INTO orphanage_donation(donor_id,cash,amount,date) VALUES ("+str(request.donor.id)+",'"+str(request.POST.get('cash'))+"','"+str(request.POST.get('amount'))+"','"+str(request.POST.get('date'))+"')")
    return render(request, 'orphanage/submitform.html')

def view_parent(request):
        data = staff.objects.all()
        return render(request,'view_parent.html',{'messages':data})
       
def submit_age(request):
    age=request.GET['age']
    data = orphan.objects.filter(adopted=0,gender=age)
    return render (request, 'view_orphan.html', {'msg':data})
def view_orphan(request):

    data = orphan.objects.filter(adopted=0)
    return render (request, 'view_age.html', {'msg':data})


def view_donor(request):
    data = donor.objects.all()
    return render  (request, 'view_donor.html', {'any':data})

def submit_cash(request):
    amountf=int(request.GET['amountfrom'])
    amountt=int(request.GET['amountto'])
    data = donation.objects.filter(cash__range=(amountf,amountt))
    return render (request, 'view_donationhistory.html', {'his':data})

def view_donationhistory(request):
    data = donation.objects.all()
    return render (request, 'view_cash.html', {'his':data})

def submit_year(request):
    year=request.GET['year']
    data = orphan.objects.filter(adopted=0,dateofbirth__year=year)
    return render (request, 'view_orphan.html', {'msg':data})
def submit_year2(request):
    year=request.GET['year']
    data = donation.objects.filter(date__year=year)
    return render (request, 'view_donationhistory.html', {'his':data})


def submit_adopt(request):
    year=request.GET['year']
    data = adoption.objects.filter(date__year=year)
    return render (request, 'view_adoptionhistory.html', {'adop':data})

def view_adoptionhistory(request):
    # year=request.POST['year']
    # data = adoption.objects.filter(date=year.year)
    data = adoption.objects.all()
    return render (request, 'view_adopt.html', {'adop':data}) 



