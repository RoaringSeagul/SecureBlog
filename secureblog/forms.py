from django import forms
from .models import Post
from .models import Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['published_date', 'Post', 'create_date']
