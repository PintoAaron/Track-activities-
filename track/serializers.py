from rest_framework import serializers
from .models import Member, Activity,Remark



class MemberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Member
        fields = ['id','user_id','first_name','last_name','bio']
        

class ActivitySerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    timestamp = serializers.DateTimeField(read_only = True)
    class Meta:
         model = Activity
         fields = ['id','title','description','status','poster','timestamp']
         
         
class RemarksSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only = True)
    activity_id = serializers.IntegerField(read_only = True)
    commenter_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Remark
        fields = ['id','activity_id','comment','commenter_id','date_created']
        
         