from django import forms
from .models import CourseNote
class CourseNoteForm(forms.ModelForm):

 class Meta:
        model = CourseNote
        fields = ['course', 'title', 'content', 'status']
        
        
        
 def clean_course(self):
        course = self.cleaned_data.get('course')
        if len(course) < 2:
            raise forms.ValidationError("Course name must be at least 2 characters long.")
        return course.upper()  
    
 def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
    
 def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("Content must be at least 10 characters long.")
        return content