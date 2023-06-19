from django.shortcuts import render, redirect


def index(request):
    profile = True
    if not profile:
        return redirect('profile-create')

    return render(request, 'home-with-profile.html')


def add_note(request):
    return render(request, 'note-create.html')


def edit_note(request, pk):
    return render(request, 'note-edit.html')


def delete_note(request, pk):
    return render(request, 'note-delete.html')


def details_note(request, pk):
    return render(request, 'note-details.html')


def profile_create(request):
    return render(request, 'home-no-profile.html')


def profile_details(request):
    return render(request, 'profile.html')
