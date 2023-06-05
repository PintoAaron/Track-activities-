from django.contrib import admin
from .models import Member,Activity,Remark

@admin.register(Member)
class MemeberAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,'user','first_name','last_name', 'bio']
    list_select_related = ['user']
    
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','status','poster','timestamp']
    list_select_related = ['poster']
    
    
    
@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ['id','comment','activity','commenter','date_created']
    list_select_related = ['activity','commenter']
