from django.db import models

# Create your models here.

class CourseNote(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('complete', 'Complete')
    ]
    
    course = models.CharField(max_length=50, help_text="Enter course code (e.g., IS424)")
    
    title = models.CharField(max_length=100, help_text="Enter a descriptive title for your note")
    
    content = models.TextField(max_length=10000, help_text="Enter your note content here")
    
    date = models.DateField(auto_now_add=True, help_text="Date will be automatically set")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    

    