import django_tables2 as tables
from mezzanine_firestore.models import Project

class Project_Table(tables.Table):
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                      template_name='mezzanine_firestore/my_column.html')
    class Meta:
        model = Project
        template_name = 'django_tables2/bootstrap.html'
        fields = ['code','title','begin_date','end_date']
        #fields = ('nombres', 'apellido_paterno', 'apellido_materno','fecha_de_nacimiento') # fields to display
        
