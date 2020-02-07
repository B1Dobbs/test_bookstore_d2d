import os

def validate_xml(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.xml']
    if not ext.lower() in valid_extensions:
        raise ValidationError('XML Files Accepted Only')
