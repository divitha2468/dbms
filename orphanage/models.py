from django.db import models

# Create your models here.
class parent(models.Model):
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
class adoption(models.Model):
    parentname=models.CharField(max_length=30,default=False)
    phno=models.CharField(max_length=10,default=False)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    orphanname=models.CharField(max_length=20)
    orphanid=models.IntegerField()
    date=models.DateField()
    class meta:
        db_table="adoption"

   
    