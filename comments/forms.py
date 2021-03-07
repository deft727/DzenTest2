from django import forms
from .models import Reviews
from captcha.fields import CaptchaField

class ReviewsForm(forms.ModelForm):
    name= forms.CharField(label='Имя', max_length=100 , widget=forms.TextInput(attrs={
                                                        'class': "form-control",
                                                        'name':'name',
                                                        'id':'contactparent'}))
    email=forms.EmailField(label='E-mail', max_length=100 , widget=forms.TextInput(attrs={'class': "form-control",
                                                                                                'name':'email'}))
    text=  forms.CharField(label='Сообщение', max_length=500 , widget=forms.Textarea(attrs={'class': "form-control",
                                                                                            'name':'text',
                                                                                            'id':'contactcomment'}))
    captcha = CaptchaField(label='Капча')


    class Meta:
        model=Reviews
        fields=[
            "name",
            "email",
            "text",
            "captcha"
        ]