from django.shortcuts import render, reverse, redirect,  get_object_or_404
from .models import Article, Category, Tag, ExtraPicture, ExtraText
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm
from profile.models import Profile
from about.models import About


def index(request):
    obj_list = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    profile = Profile.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if cat:
        obj_list = obj_list.filter(category__title__exact=cat)
    if tag:
        obj_list = obj_list.filter(tags__title__icontains=tag)
    if q:
        obj_list = obj_list.filter(title__icontains=q)
    pag = Paginator(obj_list, 2)
    page = request.GET.get('page')
    obj = pag.get_page(page)
    about = About.objects.get(id=1)

    ctx = {
        'objects': obj,
        'categories': categories,
        'tags': tags,
        'profiles': profile,
        'obj': about,
    }
    return render(request, 'blog/index.html', ctx)


def category(request):
    article = Article.objects.all()
    profile = Profile.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if cat:
        article = article.filter(category__title__exact=cat)
    if tag:
        article = article.filter(tags__title__icontains=tag)
    if q:
        article = article.filter(title__icontains=q)
    about = About.objects.get(id=1)
    ctx = {
        'object': article,
        'profiles': profile,
        'categories': category,
        'tags': tags,
        'obj': about,
    }
    return render(request, 'blog/category.html', ctx)


def post_view(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('project:detail', kwargs={'pk': pk}))


def detail(request, pk):
    obj = Article.objects.get(id=pk)
    #obj.views += 1
    #obj.save()
    form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('profile:login')
        form = CommentForm(data=request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.article = obj
            com.author_id = request.user.profile.id
            com.save()
            return redirect('.')
    article = Article.objects.all()              #order_by('-id')[:3]
    profile = Profile.objects.all()
    categories = Category.objects.all()
    tag = Tag.objects.all()
    about = About.objects.get(id=1)
    ctx = {
        'object': obj,
        'objects': article,
        'profiles': profile,
        'categories': categories,
        'tags': tag,
        'form': form,
        'obj': about,

    }
    return render(request, 'blog/blog-single.html', ctx)


def article_list(request):
    article = Article.objects.order_by('-id')
    profile = Profile.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('q')
    if cat:
        article = article.filter(category__title__exact=cat)
    if tag:
        article = article.filter(tags__title__icontains=tag)
    if search:
        article = article.filter(title__icontains=q)
    about = About.objects.get(id=1)
    ctx = {
        'object': article,
        'profiles': profile,
        'categories': category,
        'tags': tags,
        'obj': about,
    }
    return render(request, 'blog/list.html', ctx)





