from django.db import models
from django.conf import settings

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    bio = models.TextField(max_length=500, null=True, blank=True)
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name
    
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Activity(models.Model):

    PENDING_STATE = 'P'
    DONE_STATE = 'D'

    ACTIVITY_STATE = [
        (PENDING_STATE, 'Pending'),
        (DONE_STATE, 'Done')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=1, choices=ACTIVITY_STATE, default=PENDING_STATE)
    poster = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='activities')
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Remark(models.Model):
    commenter = models.ForeignKey(Member, on_delete=models.PROTECT,related_name='remarks')
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT, related_name='remarks')
    comment = models.TextField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
