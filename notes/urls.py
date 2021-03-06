from django.urls import path

from notes.views import UserViewSet, NoteCreateView, NoteListView, AuthenticateView

app_name = "note"
urlpatterns = [
    path("user/", UserViewSet.as_view(), name="create_user"),
    path("sites/list/", NoteListView.as_view(), name="view_notes"),
    path("sites/", NoteCreateView.as_view(), name="create_note"),
    path("user/auth/", AuthenticateView.as_view(), name="authenticate_user")
]
