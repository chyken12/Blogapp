from dataclasses import field
import email
from tkinter import Widget
from django import forms
from . models import Comment,Newsletter



class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name','email','message')
    
    
# class SubscribersForm(forms.ModelForm):
#   class Meta:
#     model = Subscribers
#     fields = ['email',]
    
    
class NewsletterForm(forms.ModelForm):
  class Meta:
    model =  Newsletter
    fields = ['title','message']
