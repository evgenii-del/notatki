from django import forms
# from taggit.forms import TagField
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'tags', 'body', 'image')


class NoteSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search by title or content'})
    )

    # CHOICES = [
    #     ('oldTonew', 'To new'),
    #     ('newToold', 'To old'),
    # ]
    # sort_notes = forms.ChoiceField(choices=CHOICES)
