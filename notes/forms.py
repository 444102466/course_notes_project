from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Form for creating and editing course notes.
    Uses ModelForm to automatically generate fields from the Note model.
    """
    class Meta:
        model = Note
        fields = ['course', 'title', 'content', 'status']
        widgets = {
            'course': forms.TextInput(attrs={
                'placeholder': 'e.g., IS424',
                'class': 'form-input'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Note title',
                'class': 'form-input'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter your notes here...',
                'rows': 10,
                'class': 'form-textarea'
            }),
            'status': forms.Select(attrs={
                'class': 'form-input'
            }),
        }
        labels = {
            'course': 'Course',
            'title': 'Note Title',
            'content': 'Content',
            'status': 'Status'
        }