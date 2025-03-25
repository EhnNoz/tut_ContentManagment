from django.urls import path, include
# from .views import ContentList, ContentDetail, UserList, UserDetail, ContentUpdate, ContentDestroy
from rest_framework import routers
from .views import ContentViewSet, UserViewSet, RetrieveUserView
app_name = 'api'

router = routers.SimpleRouter()
router.register('content', ContentViewSet)
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('authors/<int:pk>/', RetrieveUserView.as_view(), name='user-detail')
]
# urlpatterns = [
#     path('', ContentList.as_view(), name='list'),
#     path('<int:pk>', ContentDetail.as_view(), name='detail'),
#     path('<int:pk>/update', ContentUpdate.as_view(), name='update'),
#     path('<int:pk>/delete', ContentDestroy.as_view(), name='delete'),
#     path('user/', UserList.as_view(), name='user-list'),
#     path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
#
# ]
