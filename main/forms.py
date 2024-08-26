from django import forms


class addPostForm(forms.Form):
    card_title = forms.CharField( max_length=100)
    card_description=forms.CharField(widget=forms.Textarea)
    img_url=forms.FileField()

