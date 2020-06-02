from django import forms

class userForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"name": "username", "class": "form-control",'placeholder':'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"name": "password", "class": "form-control",'placeholder':'password'})
    )