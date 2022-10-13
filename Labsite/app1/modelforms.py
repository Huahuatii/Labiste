
from django import forms
from app1 import models

class membersModelForm(forms.ModelForm):
    class Meta:
        model = models.members
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class articlesModelForm(forms.ModelForm):
    class Meta:
        model = models.articles
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class LoginForm(forms.Form):
    admin = forms.CharField(label="管理员",widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
    password = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={"class":"form-control"}),required=True)
