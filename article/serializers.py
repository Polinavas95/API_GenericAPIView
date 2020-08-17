from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """ModelSerializer with create, update methods and validators.

    """
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')
