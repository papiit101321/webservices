from django.views.generic import View
from mezzanine_firestore.models import Project
from mezzanine_firestore.forms import Project_Form
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_tables2 import RequestConfig
from mezzanine_firestore.tables import Project_Table
from django.http import HttpResponseRedirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.core import serializers
from django.forms.models import model_to_dict
import json


class Update_View(View):
    template_name = 'mezzanine_firestore/update.html'
    #db = None #firestore.client()
    
    def __init__(self, **kwargs):
        self.db = None
        if not firebase_admin._apps:
            cred = credentials.Certificate('/home/vdelaluz/public_html/test1/mezzanine_firestore/tokens/tics2021-d589d-firebase-adminsdk-t1wqc-1970fbeb45.json')
            firebase_admin.initialize_app(cred)

    def get(self, request, *args, **kwargs):        
        # Use a service account
        self.db = firestore.client()
        #users_ref = self.db.collection(u'campaigns')
        #query_ref = cities_ref.where(u'state', u'==', u'CA')
        #docs = users_ref.stream()
        docs = self.db.collection(u'campaigns').where(u'updated', u'==', False).stream()
        firedata = []
    
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            firedata.append(f'{doc.id} => {doc.to_dict()}')
        #Empleo.objects.filter(paciente=cod_rep)
        projects = Project.objects.filter(updated=False)
        return render(request, self.template_name,{'firedata':firedata,'projects':projects})

        
    def post(self, request, *args, **kwargs):
        #export
        projects = Project.objects.filter(updated=False).values()
        self.db = firestore.client()
        for project in projects:
            project['begin_date'] = str(project['begin_date'])
            project['end_date'] = str(project['end_date'])
            project['updated'] = True
            print(project)
            #data = serializers.serialize("json",project)
            #print(data)
            #print(project['begin_date'])
            ref = self.db.collection(u'campaigns').document()
            project['firestoreID'] = ref.id
            self.db.collection(u'campaigns').document(ref.id).set(project)

            p = Project.objects.get(id=project['id'])
            p.updated = True  # change field
            p.firestoreID= ref.id
            p.save() # this will update only


        docs = self.db.collection(u'campaigns').where(u'updated', u'==', False).stream()
        
        for doc in docs:
            data = doc.to_dict()
            data.pop('id', None)
            project = Project.objects.create(**data)
            project.updated = True
            project.save()
            
            project_ref = self.db.collection(u'campaigns').document(project.firestoreID)
            project_ref.update({u'updated': True})
            project_ref.update({u'id': project.id})


            
            
        return HttpResponseRedirect('/firestore') # /<url_plugin>        
        #return render(request, self.template_name,{'firedata':firedata,'projects':projects})
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Update_View, self).dispatch(*args, **kwargs)


class ProjectList_View(View):
    template_name = 'mezzanine_firestore/project-list.html'
    
    def get(self, request, *args, **kwargs):        
        table = Project_Table(Project.objects.all())
        RequestConfig(request,paginate={'per_page': 25}).configure(table)
        return render(request, self.template_name, {'table': table})
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectList_View, self).dispatch(*args, **kwargs)



class Project_View(View):  
    initial={'key':'value'}
    form_class = Project_Form
    template_name = 'mezzanine_firestore/project.html'

    def __init__(self, **kwargs):
        self.db = None
        if not firebase_admin._apps:
            cred = credentials.Certificate('/home/vdelaluz/public_html/test1/mezzanine_firestore/tokens/tics2021-d589d-firebase-adminsdk-t1wqc-1970fbeb45.json')
            firebase_admin.initialize_app(cred)

    
    def get(self, request, *args, **kwargs):        
        project_code = self.kwargs['project_code']  
        try:
            project = Project.objects.get(code=project_code)            
            form= self.form_class(instance=project)
        except Project.DoesNotExist:
            form=self.form_class(initial=self.initial)
            #paciente_count = Paciente.objects.filter().count()
            project_code = 0 # request.user.username +'-'+ str(pacient_count)
        return render(request, self.template_name, {'form':form, 'project_code':project_code})#nos muestra el formulario para llenar
        
    def post(self, request, *args, **kwargs): 
        
        if 'cancel_page_button' in request.POST:
            return HttpResponseRedirect('/firestore') # /<url_plugin>
        
        #patient_code = self.kwargs['patient_code']
        ###
        ###if 'empleo_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/empleo-lista/')
        ###
        ###if 'apnp_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/apnp/')
        ###
        ###if 'ago_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/ago/')
        ###
        ###if 'app_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/app/')
        ###
        ###if 'ahf_button' in request.POST:
        ###    return HttpResponseRedirect('/mdrecords/'+str(cod_rep)+'/ahf/')
        ###
        if 'save_page_button' in request.POST:
            project_code = self.kwargs['project_code'] 
            #    #cod_rep = self.kwargs['cod_rep']
            try:
                instance=Project.objects.get(code=project_code)
                form = self.form_class(request.POST or None, instance=instance)            
            except Project.DoesNotExist:
                #form=self.form_class(instance=pacient)
                form = self.form_class(request.POST)       
            if form.is_valid():
                project = form.save()#commit=False)

                if (project.updated):
                    self.db = firestore.client()
                    project_ref = self.db.collection(u'campaigns').document(project.firestoreID)
                    dict_obj = model_to_dict(project)

                    dict_obj['begin_date'] = str(dict_obj['begin_date'])
                    dict_obj['end_date'] = str(dict_obj['end_date'])
            

                    #serialized = json.dumps(dict_obj,default=str)
                    project_ref.update(dict_obj)
                #print 'pacient saved'
                #pacient.id = self.kwargs['cod_rep']                
                #pacient.save()
                #return HttpResponseRedirect('/mdrecords/'+pacient.id+'/pacient-saved/')
                return render(request, 'mezzanine_firestore/project-saved.html' , {'project': project})
            else:
                print('form not valid')
                return render(request, self.template_name, {'form': form, 'project_code': project_code })
        return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Project_View, self).dispatch(*args, **kwargs)
