
from django.urls import path,include
from rest_framework_nested import routers
from .views import ActivityViewSet,MemberViewSet

router = routers.DefaultRouter()
router.register('members',MemberViewSet)
router.register('activities',ActivityViewSet)




urlpatterns = [
    path('',include(router.urls))

]
