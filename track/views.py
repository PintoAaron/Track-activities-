from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from .models import Member, Activity, Remark
from .serializers import MemberSerializer, ActivitySerializer, RemarksSerializer


class MemeberViewset(ListModelMixin,UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.select_related('user').all()
