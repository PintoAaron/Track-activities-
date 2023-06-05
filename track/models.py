from django.db import models
from django.conf import settings

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    bio = models.TextField(max_length=500, null=True, blank=True)


class Activities(models.Model):

    PENDING_STATE = 'P'
    DONE_STATE = 'D'

    ACTIVITY_STATE = [
        (PENDING_STATE, 'Pending')
        (DONE_STATE, 'Done'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField( max_length=1, choices=ACTIVITY_STATE, default=PENDING_STATE)
    poster = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='activities')
    remarks = models.TextField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
