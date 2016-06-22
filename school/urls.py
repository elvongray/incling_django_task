from rest_framework import routers

from views import ClassroomsViewSet, StudentsViewSet

router = routers.SimpleRouter()
router.register(r'classrooms', ClassroomsViewSet)
router.register(r'students', StudentsViewSet)

urlpatterns = router.urls
