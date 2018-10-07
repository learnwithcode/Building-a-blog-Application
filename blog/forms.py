from django import forms
from .models import Comment

class EmailForm(forms.Form):
  name = forms.CharField(max_length=250, 
                            widget=forms.TextInput(
                            attrs={'placeholder':'Your Name'
                            }
                          )
                        )
  email = forms.EmailField(
                            widget=forms.EmailInput(
                            attrs={'placeholder':'Your Email'
                            }
                          )
                        )
  to = forms.EmailField(                            
                            widget=forms.EmailInput(
                            attrs={'placeholder':'Reciever Email'
                            }
                          )
                        )
  message = forms.CharField(required=False,
                            widget=forms.Textarea(
                            attrs={'placeholder':'Your Comments'
                            }
                          )
                        )

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')
