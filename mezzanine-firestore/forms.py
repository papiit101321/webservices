from django.forms import ModelForm
from mezzanine_firestore.models import Project

class Project_Form(ModelForm):
     class Meta:
        model = Project
        fields = ['code','title','resume','people_on_charge','begin_date','end_date','imageURL']
        

 
