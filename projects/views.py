from django.shortcuts import render
from projects.models import Project, Category

# Create your views here.
def project_index(request):
    categories = Category.objects.all().prefetch_related('projects')
    context = {
            'categories': categories
     }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
            'project':project
    }
    return render(request, 'project_detail.html', context)

def project_category(request, category):
    #projects = Project.objects.filter(categories=category).order_by('-date')
#    category = Category.objects.filter(name__exact=category).prefetch_related('projects')
    projects = Project.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )


    context = {
            'category': category,            
            'projects':projects
    }
    return render(request, 'project_category.html', context)
