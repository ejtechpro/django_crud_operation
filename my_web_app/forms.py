from django import forms
from .models import Student
from django.forms import ModelForm, Textarea, RadioSelect, CheckboxInput,ChoiceField
from django.forms.widgets import PasswordInput


class StudentForm(forms.ModelForm):
  class Meta: 
    model = Student
    #fields = '__all__'
    fields = ('course','first_name', 'last_name','phone','gender','remarks')
    widgets = {
      'remarks': Textarea(attrs={'rows': 3}),
      'gender': RadioSelect(choices= [('male','Male'),('female','Female'),('other','Other')])
       #'gender': CheckboxInput(attrs={'id': 'gender'}),
       
    }
   
  
    
  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs) 
    self.fields['course'].empty_label = "--Choose Course--"
    #self.fields['gender'].empty_label = "--Choose Your Gender--"
  