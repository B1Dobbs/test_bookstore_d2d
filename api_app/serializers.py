from rest_framework import serializers
from .models import OnixFile

class XMLFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnixFile
        fields = "__all__"