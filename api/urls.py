from django.urls import path, include
from api.viewsets import router

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_api'))
]
