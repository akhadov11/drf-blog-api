from rest_framework import serializers

from core.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    upvotes_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = "__all__"
        # extra_kwargs = {
        #     'upvotes_count': {'read_only': True}
        # }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
