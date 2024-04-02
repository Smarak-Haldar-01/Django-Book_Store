from django import forms

class signinf(forms.Form):
    name=forms.CharField(label='Full Name',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    cr_pass=forms.CharField(label='Create Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Must Contain At Least 8 Charecters'}))
    c_pass=forms.CharField(label='Re-Enter Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    address=forms.CharField(label='Address',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address Line 1'}))
    address_2=forms.CharField(label='Address [Optional]',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address Line 2'}))
    profile_pic=forms.FileField(label='Profile Pic [Optional]',required=False,widget=forms.FileInput(attrs={'class':'form-control'}))