from django.contrib import admin
from .models import Article, Category, Tag, Comment, ExtraText, ExtraPicture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_field = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)


@admin.register(ExtraText)
class ExtraTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_date']
    date_hierarchy = 'created_date'


@admin.register(ExtraPicture)
class ExtraPictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_vite', 'created_date']
    date_hierarchy = 'created_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'author', 'created_date']
    date_hierarchy = 'created_date'


