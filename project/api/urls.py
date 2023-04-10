from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRUDAPIView, TagListCreateApiView, TagRUDAPIView,\
    ArticleListCreateAPIView, ArticleRUDAPIView, CommentListCreate, ExtrapictureListCreateAPIView, ExtraTextListCreateAPIView


urlpatterns = [
    path('category-list/', CategoryListCreateAPIView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view()),
    path('tag-list/', TagListCreateApiView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDAPIView.as_view()),

    path('article-list/', ArticleListCreateAPIView.as_view()),
    path('article-rud/<int:pk>/', ArticleRUDAPIView.as_view()),
    path('article/<int:article_id>/comment-list/', CommentListCreate.as_view()),
    path('article/<int:article_id>/content-list-create/', ExtraTextListCreateAPIView.as_view()),
    path('article/<int:article_id>/content-list-create/image/', ExtrapictureListCreateAPIView.as_view())
]
