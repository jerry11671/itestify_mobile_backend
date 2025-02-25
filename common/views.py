from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .responses import CustomResponse



class HealthCheckAPIView(GenericAPIView):
    def get(self, request):
        return CustomResponse.success(message='Server is active', status_code=200)