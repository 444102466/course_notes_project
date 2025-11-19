from django.shortcuts import render
from .models import CourseNote
from .forms import CourseNoteForm
from django.contrib import messages


# Create your views here.

def index(request):
   
    notes = CourseNote.objects.all()
    context = {
        'notes': notes,
        'total_notes': notes.count()
    }
    return render(request, 'notes/note_list.html', context)