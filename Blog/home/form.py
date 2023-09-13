from django import forms
from froala_editor.widgets import FroalaEditor
from .import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogModel
        fields = ['content']