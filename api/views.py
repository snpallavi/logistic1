from urllib import response
from django.shortcuts import render
import pkg_resources
from rest_framework.response import Response
from .models import UserRole, subscription
from .models import vehicle
from .serializers import UserRoleSerializer, vehicleSerializer,subscriptionSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class UserRoleApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = UserRole.objects.get(id=id)
            serializer = UserRoleSerializer(role)
            return Response(serializer.data)

        role = UserRole.objects.all()
        serializer = UserRoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = UserRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = UserRole.objects.get(pk=id)
        serializer = UserRoleSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = UserRole.objects.get(pk=id)
        serializer = UserRoleSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = UserRole.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})


class vehicleApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = vehicle.objects.get(id=id)
            serializer = vehicleSerializer(role)
            return Response(serializer.data)

        role = vehicle.objects.all()
        serializer = vehicleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = vehicleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = vehicle.objects.get(pk=id)
        serializer = vehicleSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = vehicle.objects.get(pk=id)
        serializer = vehicleSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = vehicle.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})

class subscriptionApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = subscription.objects.get(id=id)
            serializer = subscriptionSerializer(role)
            return Response(serializer.data)

        role = subscription.objects.all()
        serializer = subscriptionSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = subscriptionSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = subscription.objects.get(pk=id)
        serializer = subscriptionSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = subscription.objects.get(pk=id)
        serializer = subscriptionSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = subscription.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})
    