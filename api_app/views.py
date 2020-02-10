from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .models import OnixFile
from django.http import JsonResponse
from .utils import onix_parser

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileProcessView(APIView):
    
    def get(self, request, format=None):
        """
        API to process ONIX File
        """
        onix_parser.process_onix(OnixFile.load().get_path())

        #Test API call
        #onix_parser.process_onix("C:/Users/brooke.dobbins/Documents/SE5/test_bookstore_d2d/api_app/resources/large_example.xml")
        return JsonResponse({'note': 'Processing Onix'})

