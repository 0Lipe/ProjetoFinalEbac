from rest_framework import serializers
from blog.models import Post
from User.models import UserInfo
from blog.serializers import PostSerializer

class UserSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True, many=True)
    posts_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),write_only=True, many=True)

    class Meta:
        model = UserInfo
        fields = ['post','posts_id','user']
        extra_kwargs = {'post': {'required': False}}
    
    def create(self, validated_data):
        post_data = validated_data.pop('post_id')
        user_data = validated_data.pop('user')

        user = UserInfo.objects.create(user= user_data)
        for post in post_data:
            user.product.add(post)

        return user