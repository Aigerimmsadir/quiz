from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class PostSerializer(serializers.Serializer):

    title = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    body = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    like_count=serializers.IntegerField(read_only=True)
    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
    class Meta:
        model = Post
        fields = ('id','title','body','created_at','created_by')




