from django.db import models

# Create your models here.
class parent(models.Model):
    #parentid=models.IntegerField(unique=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    class meta:
        db_table="parent"
    

class orphan(models.Model):
    #orphanid=models.IntegerField(unique=True)
    orphanname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    adopted=models.IntegerField(default=0)
    # age=models.IntegerField()
    dateofbirth=models.DateField()
    class meta:
        db_table="orphan"

class donor(models.Model):
     #donorid=models.IntegerField(unique=True)
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
    parent=models.ForeignKey(parent,on_delete=models.CASCADE)
    orphan=models.ForeignKey(orphan,on_delete=models.CASCADE)
    date=models.DateField()
    class meta:
        db_table="adoption"
        unique_together = ("parent", "orphan")

class donation(models.Model):
    donor=models.ForeignKey(donor,on_delete=models.CASCADE)
    cash=models.CharField(max_length=20)
    amount=models.CharField(max_length=20)
    date=models.DateField()
    class meta:
        db_table="donation"

   
    