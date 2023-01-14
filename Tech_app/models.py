from django.db import models
from datetime import datetime 

# Create your models here.
class Service(models.Model):
    service = models.CharField(max_length=200,null=True,blank=True)
    discription = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to="images")
    service_detail_name = models.CharField(max_length=200,null=True,blank=True)
    time_required =  models.IntegerField(null=True)
    



    def __str__(self):

        return self.service

class registerDB(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)


    def __str__(self):

        return self.name 
    

class ServiceBooking(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE ,null=True)
    Aname = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length=200,null=True,blank=True)
    user = models.ForeignKey(registerDB,on_delete=models.CASCADE ,null=True)
    slot_status = models.CharField(max_length=200,default='Pending')
    booked_time = models.DateTimeField(default=datetime.now(), blank=True)
    date_for_service=models.DateField()
    
    
    def __str__(self):

        return self.Aname 
    

class Teams(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    position = models.CharField(max_length=200,null=True,blank=True)
    images = models.ImageField(upload_to="images")


    def __str__(self):

        return self.name 
    


class ServiceStatusDetail(models.Model):
    services_rendered = models.CharField(max_length=200,null=True,blank=True)
    amount	 = models.IntegerField(null=True)
    booking = models.ForeignKey(ServiceBooking,on_delete=models.CASCADE ,null=True)
   
    payment_request_id = models.CharField(max_length=300,null=True,blank=True)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    payment_status = models.CharField(max_length=100,default='pending')


    def __str__(self):

        return self.booking.user.name 



class Contact (models.Model):
    contactname=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField()
    msg=models.TextField()


    
    def __str__(self):
        return self.email
        



