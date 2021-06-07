from rest_framework import serializers
from apiapp.models import Post


# class LikeDislikeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = LikeDislike
#         fields = ('like', 'dislike')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # likes = LikeDislikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'like')


