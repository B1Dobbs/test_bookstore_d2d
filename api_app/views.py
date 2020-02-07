from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import XMLFileSerializer
import onixcheck
from .models import OnixFile
from .utils import OnixParser
from django.http import JsonResponse


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        onix_file = request.data['onix_file']

        print(request.data['onix_file'])
        
        onix_errors = onixcheck.validate(onix_file)

        if len(onix_errors) > 0:
            print("Onix Errors")
            return Response(onix_errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Success", status=status.HTTP_201_CREATED) 
        

class FileProcessView(APIView):
    
    def get(self, request, format=None):
        """
        API to process ONIX File
        """
        #TODO: call process onix here
        #process_onix(File.file)
        return JsonResponse({'note': 'Processing Onix'})

