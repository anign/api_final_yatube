from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('posts', views.PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet)
router_v1.register('groups', views.GroupViewSet)
router_v1.register('follow', views.FollowViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
