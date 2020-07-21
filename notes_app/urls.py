from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="APIs for a blog application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@ohuru.tech"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('notes.urls', namespace='notes')),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
