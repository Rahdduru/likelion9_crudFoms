from django.contrib import admin
from django.urls import path
import crudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'),
    path('detail/', crudApp.views.detail, name='detail'),
    path('read/', crudApp.views.read, name = 'read'),
    path('new/', crudApp.views.new, name='new'),
    path('edit/', crudApp.views.edit, name='edit'),
]
