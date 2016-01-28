from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length=30, required = True,
                            error_messages={'required': 'You need to have a name or something'})
    text = forms.CharField(label = 'Comment', max_length=1000, required = True,
                            error_messages={'required': 'Comment something'})


class ImageForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length=50, required=True,
                            error_messages={'required': 'Please name your masterpiece!'})
    photographer = forms.CharField(label = 'Your name', max_length=30, required=True,
                            error_messages={'required': 'You need to have a name or something'})
    description = forms.CharField(label = 'Description', max_length=4000, required=True,
                            error_messages={'required': 'Describe your picture with a few words!'})
    img = forms.ImageField(label = 'Image', required=True,
                            error_messages={'required': 'You forgot to load the image'})
