from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Member, Activity, Remark
from .serializers import MemberSerializer, ActivitySerializer, RemarksSerializer


class MemberViewSet(ListModelMixin,UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.select_related('user').all()
    permission_classes = [IsAdminUser]


class ActivityViewSet(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset =  Activity.objects.select_related('poster').all()
    permission_classes = [IsAuthenticated]
    
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    


    