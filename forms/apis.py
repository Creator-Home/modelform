from rest_framework import routers
from modelform import api_views

router = routers.DefaultRouter()
router.register(r'studentrecords', api_views.StudentRecordViewset)