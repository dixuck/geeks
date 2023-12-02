from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()


router.register('task', TaskViewSet, 'tasks')

urlpatterns = router.urls