from django.utils import timezone
from rest_framework import serializers

from blogs.models import Comments
from CustomUsers.models import User


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('message', 'post')

    def create(self, validated_data):
        request = self.context.get('request')
        return Comments.objects.create(
            author=request.user,
            sent_at=timezone.now(),
            **validated_data)

    def to_representation(self, instance):
        repres = super().to_representation(instance)
        repres['id'] = instance.id
        repres["sent_at"] = instance.sent_at
        repres['author'] = instance.author.username
        return repres


# Users
class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')