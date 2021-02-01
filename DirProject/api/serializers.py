
from rest_framework import serializers
from .models import File, Directory


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['name', 'size', 'id']


class DirSerializer(serializers.ModelSerializer):

    class Meta:
        model = Directory
        fields = ['name', 'id']
