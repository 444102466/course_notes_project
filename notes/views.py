from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from .models import Note
from .forms import NoteForm

def index(request):
    """
    Display all course notes in card grid layout.
    Read operation - lists all notes from database.
    """
    notes = Note.objects.all().order_by('-date')
    return render(request, "notes/index.html", {
        "notes": notes
    })

def confirm_delete(request, note_id):
    """
    Display confirmation page before deleting a note.
    Shows note details and asks for confirmation.
    """
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/confirm_delete.html", {
        "note": note
    })

def delete_note(request, note_id):
    """
    Delete a specific note.
    Delete operation - removes a note from the database.
    Only accepts POST requests for security.
    """
    if request.method == "POST":
        note = get_object_or_404(Note, pk=note_id)
        note.delete()
        messages.success(request, "Note deleted successfully!")
        return redirect("notes:index")
    else:
        # If not POST, redirect to confirmation page
        return redirect("notes:confirm_delete", note_id=note_id)

def add(request):
    """
    Add a new course note.
    Create operation - handles form submission and saves to database.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("notes:index"))
        else:
            return render(request, "notes/note_form.html", {
                "form": form
            })
    
    return render(request, "notes/note_form.html", {
        "form": NoteForm()
    })

def detail(request, note_id):
    """
    Display a single note's details.
    Read operation - shows one specific note.
    Also handles status updates via POST.
    """
    note = get_object_or_404(Note, pk=note_id)
    
    if request.method == "POST":
        # Handle status update
        new_status = request.POST.get('status')
        if new_status in ['completed', 'ongoing']:
            note.status = new_status
            note.save()
            return HttpResponseRedirect(reverse("notes:detail", args=[note_id]))
    
    form = NoteForm(instance=note)
    return render(request, "notes/note_details.html", {
        "note": note,
        "form": form
    })

def edit(request, note_id):
    """
    Edit an existing course note.
    Update operation - allows changing course, title, content, and status.
    """
    note = get_object_or_404(Note, pk=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("notes:detail", args=[note_id]))
        else:
            return render(request, "notes/note_form.html", {
                "form": form,
                "note": note,
                "is_edit": True,
            })

    form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {
        "form": form,
        "note": note,
        "is_edit": True,
    })