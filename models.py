from django.db import models

# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(primary_key=True,max_length=15)
    password=models.CharField(max_length=30)

class Complaint(models.Model):
    complaint_user=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    description=models.TextField(max_length=30)
    complaintDate=models.DateField(auto_now=True)
    assigned_user=models.CharField(max_length=30)
    comments=models.CharField(max_length=30)
    complaint_status=models.CharField(max_length=30)
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    

    

    


