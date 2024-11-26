from django.db import models

# Create your models here.
#schema defines the structure of the databse
#the entire schema is defined in the models.py file

class Student(models.Model):
    #id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    age =models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    file=models.FileField(null=True, blank=True)


class Product(models.Model):
    pass    


#everytime a change is made to the model file, 
#python manage.py makemigrations
#python manage.py migrate

#if i delete the 0001 file, database will crash
# #if i delete any of the migration files, django will know, bcz it creates an entry for each migration in its database. and hhence the app will crash


# everytime i hit the migrate command , it creates a state for the model and compares with the older state and thats how it knows, there are changes made to the database

class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)
