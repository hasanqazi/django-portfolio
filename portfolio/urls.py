from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog', include('blog.urls')),
    path('contact', include('contact.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]

urlpatterns += staticfiles_urlpatterns()