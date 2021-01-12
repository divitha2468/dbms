from django.db import models


# Create your models here.
class staff(models.Model):
    #parentid=models.IntegerField(unique=True)
    # firstname=models.CharField(max_length=20)
    staffname=models.CharField(max_length=20)
    # deleted=models.IntegerField(default=0)
    email=models.EmailField()
    phno=models.CharField(max_length=10)
    designation=models.CharField(max_length=30)
    pincode=models.IntegerField()
    # address=models.CharField(max_length=100)
    # city=models.CharField(max_length=20)
    # state=models.CharField(max_length=20)
    # country=models.CharField(max_length=20)
    class meta:
        db_table="parent"
class sdetails(models.Model):

    pincode=models.IntegerField()
    h_no=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    class meta:
        db_table="sdetails"
    

class orphan(models.Model):
    staff=models.ForeignKey(staff,on_delete=models.CASCADE)
    orphanname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    adopted=models.IntegerField(default=0)
    dateofbirth=models.DateField()
    

    def age(self):
            import datetime
            dob = self.dateofbirth
            tod = datetime.date.today()
            my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
            return my_age
    age=property(age)
    class meta:
        db_table="orphan"

class donor(models.Model):
     #donorid=models.IntegerField(unique=True)
     donorname=models.CharField(max_length=30)
     phno=models.CharField(max_length=10)
     email=models.EmailField()
     pincode=models.IntegerField()
    #  city=models.CharField(max_length=20)
    #  state=models.CharField(max_length=20)
    #  country=models.CharField(max_length=20)
     class meta:
        db_table="donor"
class ddetails(models.Model):
     #donorid=models.IntegerField(unique=True)
     pincode=models.IntegerField()
     h_no=models.CharField(max_length=100)
     city=models.CharField(max_length=20)
     state=models.CharField(max_length=20)
     country=models.CharField(max_length=20)
     class meta:
        db_table="ddetails"

   
class adoption(models.Model):
    donor=models.ForeignKey(donor,on_delete=models.CASCADE)
    orphan=models.ForeignKey(orphan,on_delete=models.CASCADE)
    date=models.DateField()
    class meta:
        db_table="adoption"
        unique_together = ("donor", "orphan")

class donation(models.Model):
    donor=models.ForeignKey(donor,on_delete=models.CASCADE)
    cash=models.IntegerField()
    kind=models.CharField(max_length=20)
    date=models.DateField()
    class meta:
        db_table="donation"

   
    