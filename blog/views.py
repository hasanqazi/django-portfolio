from django.shortcuts import render
from .models import Blog as blog

# Create your views here.
def showblog(request):
  blogs = blog.objects.all().order_by('date')
  return render(request, 'blog/blog.html', {'blogs':blogs})