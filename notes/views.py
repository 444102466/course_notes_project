from django.shortcuts import render, redirect, get_object_or_404
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

def note_create(request):
    
    if request.method == 'POST':
        form = CourseNoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('index')
    else:
        form = CourseNoteForm()
    
    context = {
        'form': form,
        'action': 'Create'
    }
    return render(request, 'notes/note_form.html', context)

def note_detail(request, pk):
    note = get_object_or_404(CourseNote , pk = pk)

    context ={
        'note':note
    }

    return render(request, 'notes/note_detail.html', context)