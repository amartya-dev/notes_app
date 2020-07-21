from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('notes.urls', namespace='notes')),
    path('app/users/auth', include('rest_framework.urls', namespace='rest_framework'))
]
