from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class UserData(models.Model):
    # personal info..
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    # vital signs info..
    resting_bp = models.IntegerField()
    maximum_htr = models.IntegerField()
    # medical history info..
    chest_pain = models.CharField(max_length=50)
    fasting_bs = models.IntegerField()
    exersise_ia = models.CharField(max_length=20)
    # laboratory results info..
    cholesterol = models.IntegerField()
    # diagnostic tests info...
    resting_elr = models.CharField(max_length=150)
    st_depression = models.IntegerField()
    slop_peak_exercise = models.CharField(max_length=150)
    

class DiabeteDataModel(models.Model):
    pregnancies = models.IntegerField() 
    glucose =  models.IntegerField()
    blood_pressure = models.IntegerField() 
    skin_thickness =  models.IntegerField() 
    insulin = models.IntegerField() 
    bmi = models.IntegerField() 
    diabete_pf = models.FloatField()
    age = models.IntegerField()    
        

class Messages(models.Model):
    name =  models.CharField(max_length=200)
    email = models.EmailField() 
    contact =  models.IntegerField() 
    subject = models.CharField(max_length=200) 
    message = models.TextField()  