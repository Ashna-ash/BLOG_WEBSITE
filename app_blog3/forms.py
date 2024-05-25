from django import forms

from.models import BlogPost,Comment
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'desc', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}),
            'desc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter subheading'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter content'}),
            'image': forms.FileInput(attrs={'class':'form-control-file'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Leave a comment here'}),
        }
