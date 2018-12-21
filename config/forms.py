from django import forms
from .models import *

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["title", "icon", "folder", "state", "groups", "description"]
        labels = {"title": "", "description": "", "groups": "", "icon": "", "folder": "", "state":""}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'icon':forms.Select(attrs={'class':'chosen-select','data-placeholder':'Icono'}),
            'folder':forms.Select(attrs={'class':'chosen-select','data-placeholder':'Ubicacion'}),
            'state':forms.CheckboxInput(attrs={'class':'custom-control-input','placeholder':'Estado'}),
            'groups':forms.SelectMultiple(attrs={'class':'chosen-select','data-placeholder':'Permisos','multiple':''}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Descripcion'}),
        }
        error_messages = {"title": {"unique": "Ya existe un componente con ese titulo."}}