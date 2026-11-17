from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from accounts.models import User

class AdminSignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_superuser(**cleaned_data,role="admin")

            serializer_instance = UserSerializer(instance)

            return Response(serializer_instance.data)

        else:return Response(serializer.errors)

class StudentSignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(serializer_instance.data)

        else:return Response(serializer.errors)

class TrainerSignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(**cleaned_data,role="trainer")

            serializer_instance = UserSerializer(instance)

            return Response(serializer_instance.data)

        else:return Response(serializer.errors)

