from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework import generics



class PeoplePost(APIView):

    def post(self, request, format=None):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success", "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message":"failed"}, status=status.HTTP_400_BAD_REQUEST)

class PeopleView(APIView):
    def get(self, request, format=None):
        job = People.objects.all().order_by('-id')
        serializer = PeopleSerializer(job, many=True)
        return Response({"results":serializer.data})

class SearchPeople(generics.ListAPIView):
    serializer_class = PeopleSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = People.objects.all()
        search = self.request.query_params.get('name', None)
        if search is not None:
            queryset = queryset.filter(name__contains=search)
        return queryset

class PeopleSearch(APIView):
   def get(self, request,peoplename, format=None):
       job = People.objects.filter(name__contains=peoplename)
       serializer = PeopleSerializer(job, many=True)
       return Response(serializer.data)
    # def get_queryset(self):
    #     queryset = People.objects.all()
    #     name = self.request.query_params.get('name', None)
    #     if name is not None:
    #         queryset = queryset.filter(name=name)
    #     return queryset

class PeoplePut(APIView):
    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        peoples = self.get_object(pk)
        serializer = PeopleSerializer(peoples, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeopleDelete(APIView):

    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        peopledata = self.get_object(pk)
        peopledata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
