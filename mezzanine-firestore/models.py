from django.db import models
from django_countries.fields import CountryField

class Project(models.Model):
    code = models.CharField(max_length=256,unique=True)
    firestoreID = models.CharField(max_length=128,unique=True,blank=True,null=True)
    title = models.CharField(max_length=256)
    resume = models.CharField(max_length=1024)
    people_on_charge = models.CharField(max_length=128)
    begin_date = models.DateField()
    end_date = models.DateField()
    imageURL = models.URLField(max_length=512, blank=True,null=True)
    updated = models.BooleanField(default=False, blank=True)
    
class Visit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code = models.CharField(max_length=256,unique=True)
    firestoreID = models.CharField(max_length=128,unique=True,blank=True,null=True)
    title = models.CharField(max_length=256)
    people_on_charge = models.CharField(max_length=128)
    date = models.DateField()
    geoposition = models.CharField(max_length=128)
    updated = models.BooleanField(default=False, blank=True)

class Photo(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    firestoreID = models.CharField(max_length=128,unique=True,blank=True,null=True)
    filepath = models.CharField(max_length=512)
    imageURL = models.CharField(max_length=512)

class Label(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

class Questionary(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    quiz = models.CharField(max_length=4096)
    answers = models.CharField(max_length=4096)
    

#class Patient(models.Model):
#    
#    GENERO_CHOICES = (
#        ('1', 'Masculino'),
#        ('2', 'Femenino'),
#        ('3', 'Otro'),
#    )
#    
#    firstName = models.CharField(max_length=128)  
#    lastName = models.CharField(max_length=128)
#    gender = models.CharField(max_length=16, choices=GENERO_CHOICES) #Masculino, Femenino, Otro
#    genero_otro = models.CharField(max_length=32,blank=True,null=True) 
#    birtday = models.DateField()
#    coutry = CountryField()
#
