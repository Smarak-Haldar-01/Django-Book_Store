from django import forms

class add_product(forms.Form):
    name=forms.CharField(label="Product Name",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Product Title'}))
    details=forms.CharField(label='Product Details',required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Product Info','style':'resize:none'}))
    price=forms.CharField(label='Product Price',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Product Price'}))
    offers=forms.CharField(label='Product Offers [Optional] ',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'List Offers If Any'}))
    pic=forms.FileField(label='Product Picture [Main] ',required=True,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    pic2=forms.FileField(label='Product Picture [Optional] :',required=False,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    pic3=forms.FileField(label='Product Picture [Optional] ',required=False,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    pic4=forms.FileField(label='Product Picture [Optional] ',required=False,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    pic5=forms.FileField(label='Product Picture [Optional] ',required=False,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    edoc=forms.FileField(label='Downloadable Document',required=True,widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))