from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permission import IsAdminUserOrReadOnly, IsAuthenticatedOrReadOnly
from ..models import Category, Tag, ExtraText, ExtraPicture, Article, Comment
from .serializer import CategorySerializer, TagSerializer, ArticlePostSerializer, ArticleGetSerializer, \
    ExtraTextSerializer, ExtraPictureSerializer, CommentSerializer, MiniExtraTextSerializer, MiniExtraPictureSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagListCreateApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    # serializer_class = ArticleGetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArticleRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


class ExtraTextListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExtraText.objects.all()

    def get_queryset(self):
        extext = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            extext = extext.filter(article_id=article_id)
            return extext
        return []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MiniExtraTextSerializer
        return ExtraTextSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class ExtrapictureListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExtraPicture.objects.all()
    serializer_class = ExtraPictureSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def create(self, *args, **kwargs):

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx
