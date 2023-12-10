from django import forms


class CategoryForms(forms.Form):
    name = forms.CharField(max_length=250)


class ProductForms(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    img = forms.ImageField()


class ReviewForms(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
