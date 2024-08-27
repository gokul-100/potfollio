from django import forms

from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text','post']

class addPostForm(forms.ModelForm):
    card_title = forms.CharField( max_length=100)
    card_description=forms.CharField(widget=forms.Textarea)
    img_url=forms.FileField()
    # author = forms.fo
    class Meta:
        model = Post
        fields = ['author','tags']
