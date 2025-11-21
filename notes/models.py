from django.db import models

class Note(models.Model):
    """
    Model representing a course note.
    Fields: course, title, content, date, status
    """
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'On going'),
    ]
    
    course = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    
    def __str__(self):
        return f"{self.course}: {self.title}"