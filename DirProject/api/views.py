
# Create your views here.
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .serializers import FileSerializer, DirSerializer
from .models import File, Directory
from django.db import IntegrityError


class AddFile(APIView):
    'Api for adding file, plesase provide the following json (values are for example only){ "name": "falafel", "size":5, "parentDir":"ReadyDir"}'

    def post(self, request, format=None):
        parent_dir = request.data.get('parentDir', None)
        size = request.data.get('size', 0)
        name = request.data.get('name', None)
        if name is None:
            return Response({'error': 'missing file name'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if parent_dir is None:
            directory = Directory.objects.first()
        else:
            try:
                directory = Directory.objects.get(name=parent_dir)
            except Exception as e:
                directory = None   
        if directory is None:
           return Response({'error': ' the fileSystem need at least one directory in order to save file, please  a directory at http://localhost:8000/api/addDir'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)     
        try:
            new_file = File(name=name, size=size, directory=directory)
            new_file.save()
        except Exception as e:
            if "UNIQUE" in str(e):
                return Response({'error': 'name already exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'save file error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'newFile': FileSerializer(new_file).data}, status=status.HTTP_200_OK)


class AddDirectory(APIView):
    'Api for adding directory, plesase provide the following json (values are for example only) { "name": "Proj", "parentDir":"ReadyDir"}'
    'if there are no directories, the created directory will become the root directory.'
    def post(self, request, format=None):
        parent_dir_name = request.data.get('parentDir', None)
        name = request.data.get('name', None)
        if name is None:
            return Response({'error': 'missing new directory name'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
       # in case user havent given parentDir  the root directory will be the parent  directory
       
        if parent_dir_name is None:
            parent_directory = Directory.objects.first()
        else:
            parent_directory = Directory.objects.filter(name=parent_dir_name).first()
        try:
            new_directory = Directory(name=name, parent_directory=parent_directory)
            new_directory.save()
        except Exception as e:
            if "UNIQUE" in str(e):
                return Response({'error': ' directory nname already exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'save directory error'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'newDir': DirSerializer(new_directory).data}, status=status.HTTP_200_OK)


class ShowSystem(APIView):

    def show_directory(self, directory):
        # in case file system is completly empty
        if directory is None:
            return {}
        dir_data = {}
        dir_data['directoryName'] = directory.name
        dir_data['files'] = []
        dir_data['directories'] = []
        files = directory.files.all()
        for file_ in files:
            dir_data['files'].append(file_.name)
        sub_directories = Directory.objects.filter(parent_directory=directory)
        for sub_directory in sub_directories:
            dir_data['directories'].append(self.show_directory(sub_directory))
        return dir_data

    def get(self, req):
        data = {}
        try:
            data = self.show_directory(Directory.objects.first())
        except Directory.DoesNotExist:
            pass
        return Response(data, status=status.HTTP_200_OK)


class DeleteFile(APIView):
    'Api for deleting file, plesase provide the following json{ "name":"exampleFile"}'

    def post(self, request, format=None):

        name = request.data.get('name', None)
        if name is None:
            return Response({'error': 'missing file name to delete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # in case user havent given parentDir  the root directory will be the parentDir
        try:
            file_to_delete = File.objects.get(name=name)
            file_to_delete.delete()
        except File.DoesNotExist:
            return Response({'error': 'file name dosent exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'deleted': True}, status=status.HTTP_200_OK)


class DeleteDirectory(APIView):
    'Api for deleting directory, plesase provide the following json{ "name":"exampleFile"}'

    def post(self, request, format=None):

        name = request.data.get('name', None)
        if name is None:
            return Response({'error': 'missing directory name to delete'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # in case user havent given parentDir  the root directory will be the parentDir
        try:
            directory_to_delete = Directory.objects.get(name=name)
            directory_to_delete.delete()
        except Directory.DoesNotExist:
            return Response({'error': 'directory  dosent exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'deleted': True}, status=status.HTTP_200_OK)
