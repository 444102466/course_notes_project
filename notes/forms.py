from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

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


        def clean_course(self):
            course = self.cleaned_data.get('course')
            if len(course) <= 2:
                raise forms.ValidationError("Course name must be at least 2 characters long.")
            return course.upper()

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if len(title) <= 2:
                raise forms.ValidationError("Title must be at least 2 characters long.")
            return title

        def clean_content(self):
            content = self.cleaned_data.get('content')
            if len(content) <= 10:
                raise forms.ValidationError("Content must be at least 10 characters long.")
            return content