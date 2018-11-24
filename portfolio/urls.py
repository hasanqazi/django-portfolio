from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog', include('blog.urls'))
]
