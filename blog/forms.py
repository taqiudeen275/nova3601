from django import forms
from .models import Comment, Post,Category,Author
from froala_editor.widgets import FroalaEditor
from account.models import User


class CommentForm(forms.ModelForm):
    content = forms.CharField(label=False,widget=forms.Textarea(
        attrs={

            'class': "form-control mb-10",
            'id': "comment",
            'cols': '30',
            'rows': '9',
            'placeholder': 'Write Comment'
        }
    ))

    class Meta:
        model = Comment
        fields = ('content',)

class CategoryForm(forms.ModelForm):
    title = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "input-material",
            'placeholder': 'Category'
        }
    ))

    
    class Meta:
        model = Category
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
        'user': forms.Select(attrs={'class': 'input-material'}),
        }


class PostForm(forms.ModelForm):
    title = forms.CharField(label=False,widget=forms.TextInput(
        attrs={

            'class': "input-material",
            'placeholder': 'Title'
        }
    ))
    overview = forms.CharField(label=False,widget=forms.Textarea(
        attrs={

            'class': "input-material p-2",
            'placeholder': 'overview'
        }
    ))
    content = FroalaEditor()
   
 
    class Meta:
        model = Post 
       
        fields = ('title', 'thumbnail', 'overview', 'content', 'categories', 'featured') 