from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note


def home_view(request):
    notes = Note.objects.all()
    return render(request, 'main/home.html', {'notes': notes})


@login_required
def dashboard_view(request):
    user_notes = Note.objects.filter(author=request.user)
    return render(request, 'main/dashboard.html', {'notes': user_notes})


@login_required
def note_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            Note.objects.create(title=title, content=content, author=request.user)
            messages.success(request, 'Жазба сәтті қосылды!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Тақырып пен мазмұнды толтырыңыз.')
    return render(request, 'main/note_form.html', {'action': 'Қосу'})


@login_required
def note_edit_view(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            note.title = title
            note.content = content
            note.save()
            messages.success(request, 'Жазба сәтті өзгертілді!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Тақырып пен мазмұнды толтырыңыз.')
    return render(request, 'main/note_form.html', {'note': note, 'action': 'Өзгерту'})


@login_required
def note_delete_view(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Жазба жойылды.')
        return redirect('dashboard')
    return render(request, 'main/note_confirm_delete.html', {'note': note})
