from rest_framework import serializers
from .models import OnixFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnixFile
        fields = "__all__"