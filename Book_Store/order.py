from django import forms

class order(forms.Form):
    email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}))
    order_name=forms.CharField(label='Order Name',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Order Item Name'}))
    order_details=forms.CharField(label='Order Details [Optional] ',required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Item Details','style':'resize:none;'}))
    ex_order_delvery=forms.DateField(label='When You Want It To Be Delivered ? Format [YYYY-MM-DD]',required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Delivery Date'}))
    ex_order_time=forms.TimeField(label='At What Time Should We Sent ? Format [HH:MM]',required=False,widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Delivery Time'}))