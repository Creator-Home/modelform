from rest_framework import routers
from modelform import api_views
from modelform.views import CustomStatusViewSet, StudentStatusViewSet

router = routers.DefaultRouter()
router.register(r'studentrecords', api_views.StudentRecordViewset)
router.register(r'customrecords', CustomStatusViewSet, basename="customrecord")
router.register(r'StudentStatusViewSet', StudentStatusViewSet, basename="StudentStatusViewSet")