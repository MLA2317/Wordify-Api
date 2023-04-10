from django.urls import path
from .views import index, detail, category, article_list, post_view
from about.urls import about

app_name = 'project'


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('detail/views/<int:pk>/', post_view, name='post_view'),
    path('category/', category, name='category'),
    #path('about/', about, name='about'),
    path('list/', article_list, name='list')
]