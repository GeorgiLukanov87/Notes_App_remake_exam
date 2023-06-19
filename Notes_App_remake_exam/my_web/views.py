from django.shortcuts import render, redirect

from Notes_App_remake_exam.my_web.forms import ProfileCreateForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from Notes_App_remake_exam.my_web.models import Profile, Note


def index(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('profile-create')

    notes = Note.objects.all().order_by('id')

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = CreateNoteForm()
    else:
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'profile.html', context)


def profile_delete(request):
    Profile.objects.first().delete()
    Note.objects.all().delete()
    return redirect('index')
