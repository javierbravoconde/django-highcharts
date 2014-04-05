from django import forms

class ContactForm(forms.Form):    
    inputvalue = forms.CharField(required=False)
    outputvalue = forms.CharField(required=False)
    