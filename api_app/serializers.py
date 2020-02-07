from rest_framework import serializers
from .models import OnixFile
from .validators import validate_xml

class XMLFileSerializer(serializers.Serializer):
    onix_file = serializers.FileField(validators=[validate_xml])
