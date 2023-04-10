from django.shortcuts import render, redirect
from profile.models import Profile
from .forms import ContactForm
from about.models import About
from project.models import Article, Category, Tag


def index(request):
    profile = Profile.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('.')
    author = Article.objects.all()
    about = About.objects.get(id=1)
    if form.is_valid():
        form.save()

    ctx = {
        'form': form,
        'profiles': profile,
        'objects': author,
        'categories': category,
        'tags': tag,
        'obj': about,
    }
    return render(request, 'blog/contact.html', ctx)


