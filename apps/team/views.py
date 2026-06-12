from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import (TeamSerializer, CareerFilterSerializer, CareerFilterResponseSerializer,
)
from .models import MajorTeam,Career
from rest_framework.response import Response
from rest_framework import status
import requests
import httpx
from django.http import JsonResponse


# Create your views here.


class TeamViewSet(ModelViewSet):
    queryset = MajorTeam.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        instance.delete()

        return Response(
            {
                "message": "Team deleted successfully"
            },
            status=status.HTTP_200_OK
        )

class CareerFilterView(APIView):

    def post(self, request):
        serializer = CareerFilterSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        filters = serializer.validated_data
        queryset = Career.objects.all()
        if "is_active" in  filters:
            queryset = queryset.filter(is_active=filters["is_active"])
        if "age" in filters:
            queryset = queryset.filter(user__age=filters["age"])
        if "team" in filters:
            queryset = queryset.filter(team=filters["team"])
        if "user" in filters:
            queryset = queryset.filter(user__email=filters["user"])
        if "goals" in filters:
            queryset = queryset.filter(goals=filter['goals'])

        response_serializer = CareerFilterResponseSerializer(queryset,many=True)
        return Response(response_serializer.data,status=status.HTTP_200_OK)
        


class WeatherCheck(View):
    async def get(self,request):
        url = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-01-01&hourly=temperature_2m"
        async with httpx.AsyncClient() as client:
            out = await client.get(url)
        print(out,"out")
        return JsonResponse(out.json())




async def weather(request):
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-01-01&hourly=temperature_2m"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return JsonResponse(response.json())