from rest_framework import serializers
from blog.models import Content
from django.contrib.auth.models import User
from drf_dynamic_fields import DynamicFieldsMixin


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        # exclude = ['slug']
        # fields = '__all__'


class AuthorUsernameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class ContentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    def get_author(self, obj):
        return {obj.author.username,
                obj.author.email}

    # author = AuthorSerializer()
    # author = serializers.HyperlinkedRelatedField(read_only=True, view_name='api:user-detail')
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.email")
    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Content
        # fields  = ['title','author','description','publish']
        # exclude = ['slug']
        fields = '__all__'

    def validate_title(self, value):

        block_list = ['شهرزاد', 'قهوه تلخ']
        for item in block_list:
            if item in value:
                raise serializers.ValidationError("محتوا خارجی است.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields  = ['title','author','description','publish']
        # exclude = ['slug']
        fields = '__all__'
