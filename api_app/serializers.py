from rest_framework import serializers
from .models import OnixFile
from .validators import validate_xml

class XMLFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnixFile
        fields = "__all__"
