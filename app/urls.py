from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload_file'),
    path('converted/<int:pk>/', views.converted_document, name='converted_document'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)