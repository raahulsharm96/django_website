from django import forms
from .models import Resume

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ResumeForm(forms.ModelForm):
    class Meta:
        model= Resume
        fields=["fname", "lname","email","age","skills","CTC","Experience","resume"]