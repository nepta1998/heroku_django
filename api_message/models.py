from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(
        upload_to='pictures/%y/%m/%d/',
        default='pictures/default.jpg',
        max_length=255
    )


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'image', 'pk')
