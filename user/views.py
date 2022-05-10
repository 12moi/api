from django.shortcuts import render
from user.models import Apply
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import  viewsets
from user.serializer import ApplySerializer

# Create your views here.
class ApplyViewSet(viewsets.ModelViewSet):  
      serializer_class = ApplySerializer
      queryset = Apply.objects.all()