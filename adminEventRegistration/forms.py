from django import forms
from .models import Announcements

class userForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"name": "username", "class": "form-control",'placeholder':'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"name": "password", "class": "form-control",'placeholder':'password'})
    )

class announcementsForm(forms.ModelForm):
    location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Add Location",
                "class": "w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2",
            }
        ),
    )
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type":'date',
                "class": "w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2",
            }
        ),
    )
    req = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Add requirements of event",
                "class": "w-full bg-gray-100 rounded border border-gray-400 focus:outline-none h-48 focus:border-indigo-500 text-base px-4 py-2 resize-none block",
            }
        ),
    )
    info = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Add details of event",
                "class": "w-full bg-gray-100 rounded border border-gray-400 focus:outline-none h-48 focus:border-indigo-500 text-base px-4 py-2 resize-none block",
            }
        ),
    )
    class Meta:
        model = Announcements
        fields = [
            "info",
            "location",
            "date",
            'req'
        ]