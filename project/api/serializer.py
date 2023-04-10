from rest_framework import serializers
from ..models import Category, Tag, Article, ExtraText, Comment, ExtraPicture


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniExtraPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraPicture
        fields = ['id', 'image', 'is_vite']


class MiniExtraTextSerializer(serializers.ModelSerializer):
    extraimage = MiniExtraPictureSerializer(read_only=True, many=True)

    class Meta:
        model = ExtraText
        fields = ['id', 'description', 'extraimage']
        extra_kwargs = {
            "article": {"required": False}
        }


class ArticleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    extratext = MiniExtraTextSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'image', 'extratext', 'tags', 'views', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'tags', 'views', 'created_date']

    def create(self, validated_data):
        requests = self.context.get('request')
        author = requests.user.profile
        instance = super().create(validated_data)  #  super ota classdagi malumotni chaqirib keyin davom etirardi pasdagi kodni
        print(validated_data)
        instance.author = author
        instance.save()
        return instance


class ExtraPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraPicture
        fields = ['id', 'article_text', 'image', 'is_vite', 'created_date']


class ExtraTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraText
        fields = ['id', 'article', 'description', 'created_date']
        extra_kwargs = {
            "article": {"required": False}
        }

    def create(self, validated_data):
        extrapicture_id = self.context['extrapicture_id']
        image = validated_data.get('image')
        instance = ExtraPicture.objects.create(extrapicture_id=extrapicture_id, image=image)
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance

