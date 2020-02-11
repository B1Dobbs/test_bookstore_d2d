from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import XMLFileSerializer
from .models import OnixFile
import onixcheck
from .utils import OnixParser
from django.http import JsonResponse


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        singleton_instance = OnixFile.objects.get(id=1)
        file_serializer = XMLFileSerializer(instance=singleton_instance, data=request.data)

        if(file_serializer.is_valid()):
            
            onix_file = request.data['onix_file']
            onix_errors = onixcheck.validate(onix_file)
            if len(onix_errors) > 0:
                file_serializer.save()
                print("Onix Errors")
                return Response(onix_errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                file_serializer.save()
                print(OnixFile.load())
                return Response(OnixFile.load().__str__(), status=status.HTTP_201_CREATED)
        
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileProcessView(APIView):
    
    def get(self, request, format=None):
        """
        API to process ONIX File
        """
        #TODO: call process onix here
        #process_onix(File.file)
        return JsonResponse({'note': 'Processing Onix'})

