from django.urls import path, include

from Notes_App_remake_exam.my_web.views import index, add_note, edit_note, delete_note, details_note, profile_details, \
    profile_create, profile_delete

urlpatterns = (
    path('', include([
        path('', index, name='index'),
        path('add/', add_note, name='add-note'),

        path('edit/<int:pk>/', edit_note, name='edit-note'),
        path('delete/<int:pk>/', delete_note, name='delete-note'),
        path('details/<int:pk>/', details_note, name='details-note'),

    ])),

    path('profile/', profile_details, name='profile-details'),
    path('profile/create/', profile_create, name='profile-create'),
    path('profile/delete/', profile_delete, name='profile-delete'),
)

"""
http://localhost:8000/ - home page

http://localhost:8000/add - add note page
http://localhost:8000/edit/1 - edit note page
http://localhost:8000/delete/1 - delete note page
http://localhost:8000/details/1 - note details page

http://localhost:8000/profile - profile page
http://localhost:8000/profile/create/ - profile page
"""
