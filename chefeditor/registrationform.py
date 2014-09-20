import re
from django import forms
from chefeditor.models import Users
from chefeditor.models import Login
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_name(self):
        try:
            user = Users.objects.get(name=self.cleaned_data['name'])
        except Users.DoesNotExist:
            return self.cleaned_data['name']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean_email(self):
        try:
            user = Login.objects.get(email=self.cleaned_data['email'])
        except Login.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists."))
 
    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
    
    class Meta:
        model = Login
    
    def save(self):
        data = self.cleaned_data
        login = Login(email=data['email'],password=data['password'])
        l=login.save()
        return login
    
    

               
   