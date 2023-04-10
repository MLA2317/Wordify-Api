from django.shortcuts import render
from .models import About
from project.models import Tag, Category, Article
from profile.models import Profile


def about(request):
    obj = About.objects.get(id=1)
    obj_list = Article.objects.all()
    profile = Profile.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'obj': obj,
        'profiles': profile,
        'objects': obj_list,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/about.html', ctx)
