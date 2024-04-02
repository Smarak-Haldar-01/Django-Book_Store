from django import forms

class login(forms.Form):
    email=forms.EmailField(label="Email",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password=forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))