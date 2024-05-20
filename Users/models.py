from django.db import models
from datetime import datetime
# Create your models here.

class user(models.Model):
    uname=models.CharField(max_length=30,null=False)
    email=models.EmailField(unique=True,null=False)
    password=models.CharField(max_length=20,null=False)
    address=models.TextField(null=False)
    pic=models.FileField(upload_to="profile_pic/",max_length=250,null=True,default=None)
    user_type=models.CharField(max_length=10,null=False,default='Client')
    user_auth=models.IntegerField(default=1)
    user_code=models.IntegerField(default=101086)

class product(models.Model):
    name=models.CharField(max_length=100,null=False)
    details=models.TextField(max_length=250,null=False)
    product_price=models.FloatField(default=50)
    product_type=models.CharField(max_length=20,null=False)
    product_added_time=models.DateTimeField(auto_now_add=True)
    product_offers=models.CharField(max_length=150,default='No Offers For Now')
    pic=models.FileField(upload_to='products/',max_length=250,null=False)
    pic2=models.FileField(upload_to='products/',max_length=250,null=True)
    pic3=models.FileField(upload_to='products/',max_length=250,null=True)
    pic4=models.FileField(upload_to='products/',max_length=250,null=True)
    pic5=models.FileField(upload_to='products/',max_length=250,null=True)
    edoc=models.FileField(upload_to='downloadable/',max_length=350,null=False)

class ordered(models.Model):
    uid=models.ForeignKey(user, to_field='id', on_delete=models.CASCADE)
    umail=models.EmailField(null=False)
    order_name=models.CharField(max_length=30,null=False)
    order_details=models.TextField(default='No Details')
    ex_order_delevery=models.DateField(null=True)
    ex_order_delevery_time=models.TimeField(null=True)
    order_date=models.DateTimeField(auto_now_add=True)

class reportProblem_1(models.Model):
    uid=models.ForeignKey(user, to_field='id', on_delete=models.CASCADE)
    umail=models.EmailField(null=False)
    utype=models.CharField(max_length=20,null=False)
    report_title=models.TextField(null=False)
    explain=models.TextField(null=False)
    problem_pic=models.FileField(upload_to='problems/',max_length=250,null=True)
    problem_date=models.DateField(null=False)
    problem_time=models.TimeField(null=False)
    report_date=models.DateTimeField(auto_now_add=True)

class updated_last_profile(models.Model):
    uid=models.ForeignKey(user,to_field='id',on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)