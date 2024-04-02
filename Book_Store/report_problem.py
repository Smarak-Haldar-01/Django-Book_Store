from django import forms

class report_problem(forms.Form):
    email=forms.EmailField(label='Your Email',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}))
    report_title=forms.CharField(label='Report Title',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Report Name'}))
    report_details=forms.CharField(label='Report Details [Optional] ',required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Report Details','style':'resize:none;'}))
    problem_date=forms.DateField(label='Which Date The Problem Occured ? Format [YYYY-MM-DD]',required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Problem Occured Date'}))
    problem_time=forms.TimeField(label='At What Time the Problem Occured  ? Format [HH:MM]',required=False,widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Problem Occured Time'}))
    report_pic=forms.FileField(label='Problem Related Pic [Optional]',required=False,widget=forms.FileInput(attrs={'class':'form-control'}))