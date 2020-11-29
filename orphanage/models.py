from django.db import models

# Create your models here.
class parent(models.Model):
    parentid=models.IntegerField()
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    pincode=models.IntegerField()
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    class meta:
        db_table="parent"

class orphan(models.Model):
    orphanid=models.IntegerField()
    orphanname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    dateofbirth=models.DateField()
    class meta:
        db_table="orphan"

class donor(models.Model):
     donorid=models.IntegerField()
     donorname=models.CharField(max_length=30)
     donor_phno=models.CharField(max_length=10)
     donor_email=models.EmailField()
     address=models.CharField(max_length=100)
     city=models.CharField(max_length=20)
     state=models.CharField(max_length=20)
     country=models.CharField(max_length=20)
     class meta:
        db_table="donor"
   
class adoption(models.Model):
    parentid=models.IntegerField()
    parentfname=models.CharField(max_length=30)
    parentlname=models.CharField(max_length=30)
    phno=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    orphanname=models.CharField(max_length=20)
    orphanid=models.IntegerField()
    date=models.DateField()
    class meta:
        db_table="adoption"

class donation(models.Model):
    donorid=models.CharField(max_length=20)
    cash=models.CharField(max_length=20)
    amount=models.CharField(max_length=20)
    date=models.DateField()
    class meta:
        db_table="donation"

   
    