from django.urls import path, include
from .views import ContentList, ContentDetail

app_name = 'blog'

urlpatterns = [
    path('', ContentList.as_view(), name = 'list'),
    path('<int:pk>', ContentDetail.as_view(), name = 'detail'),

]