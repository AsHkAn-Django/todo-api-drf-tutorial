from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', views.TaskViewSet, basename='tasks')

urlpatterns = router.urls


# urlpatterns = [
#     path('', views.TaskList.as_view()),
#     path('edit/<int:pk>/', views.TaskDetail.as_view()),
# ]