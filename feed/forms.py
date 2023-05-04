from django import forms
from .models import Comments, Post
from django.forms import fields  


class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'pic', 'tags']

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

