from django import forms
from .models import User
from django.contrib.auth import  authenticate,login,logout




class SignupForm(forms.ModelForm):
    
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'"username',
      'placeholder':'username'
      
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'input-material',
      'id':'password',
       'name':'password',
       'placeholder': 'password'
         
      }))
   
   
   class Meta:
      model = User
      fields=[
         'username',    
         'password',
      ]
     

   def clean(self,*args, **kwargs):
         email = self.cleaned_data.get('email')
         username = self.cleaned_data.get('username')
         if email != '':
            emailqs = User.objects.filter(email=email)
            if emailqs.exists():
               raise forms.ValidationError('Email is already being used')
         usernameqs = User.objects.filter(username=username)
         if usernameqs.exists():
            raise forms.ValidationError('This user name is already being used. You can try adding a number to it ')
         return super(SignupForm,self).clean(*args, **kwargs)
  

class LoginForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'login-username',
      "name":"Username",
      'placeholder': 'Username or Email',
      'data-msg':"Please enter your username"
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'input-material',
      'id':'login-password',
       'name':'Password',
       'placeholder': 'Password'
         
      }))

   def clean(self,*args, **kwargs):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')

      if username and password:
         user = authenticate(username=username,password=password)
         if not user:
            raise forms.ValidationError('Incorrect Username or Password')
         

      return super(LoginForm,self).clean(*args, **kwargs)

