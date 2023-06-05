
from django.urls import path,include
from rest_framework_nested import routers
from .views import ActivityViewSet,MemberViewSet,RemarksViewSet

router = routers.DefaultRouter()
router.register('members',MemberViewSet)
router.register('activities',ActivityViewSet)


Activity_router = routers.NestedDefaultRouter(router,'activities',lookup ='activity')
Activity_router.register('remarks',RemarksViewSet,basename='activity-remarks')




urlpatterns = [
    path('',include(router.urls)),
    path('',include(Activity_router.urls))

]
