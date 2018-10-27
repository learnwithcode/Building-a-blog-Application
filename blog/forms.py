from django import forms
from .models import Comment

class EmailForm(forms.Form):
  name = forms.CharField(label=('Your Name'), max_length=250, 
                            widget=forms.TextInput(
                            attrs={}
                          )
                        )
  email = forms.EmailField(label='Your Email',
                            widget=forms.EmailInput(
                            attrs={'class':'validate'}
                          )
                        )
  to = forms.EmailField( label='Receiver Email',                           
                            widget=forms.EmailInput(
                            attrs={'class':'validate'}
                          )
                        )
  message = forms.CharField(label='Comment', required=False,
                            widget=forms.Textarea(
                            attrs={'class':'materialize-textarea'}
                          )
                        )

class CommentForm(forms.ModelForm):
    name = forms.CharField(label=('Name'), max_length=250, 
                          widget=forms.TextInput(
                          attrs={}
                        )
                      )
    email = forms.EmailField(label='Email',
                          widget=forms.EmailInput(
                          attrs={'class':'validate'}
                        )
                      )

    body = forms.CharField(label='Comment', required=False,
                          widget=forms.Textarea(
                          attrs={'class':'materialize-textarea'}
                        )
                      )
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
  search = forms.CharField(label='', 
                                widget=forms.TextInput(
                                attrs={ 'type':'search'
                                }
                              )
                            )