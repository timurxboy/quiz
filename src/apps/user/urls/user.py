from django.urls import include, path
from ..views.user import UserCreateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', UserCreateView.as_view(), name='register')
]
