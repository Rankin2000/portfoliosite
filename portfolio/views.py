from django.shortcuts import render
from projects.models import Project
from blog.models import Post

def index(request):
    recentprojects = Project.objects.all().order_by('-date')[:5]
    recentblog = Post.objects.all().order_by('-created_on')[:5]
    context = {
        'recentprojects': recentprojects,
        'recentblog': recentblog,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
