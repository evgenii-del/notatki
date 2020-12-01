from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body', 'image')


class NoteSearchForm(forms.Form):
    search_title = forms.CharField(
        required=False,
        label='Search title of your Note!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

    search_text = forms.CharField(
        required=False,
        label='Search text!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )
