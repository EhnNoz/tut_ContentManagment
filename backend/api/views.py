# from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveDestroyAPIView
from blog.models import Content
from .permissions import IsSuperUser, IsStafOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from .serializers import ContentSerializer, UserSerializer, AuthorSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Create your views here.


# class ContentList(ListCreateAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
#
#
# class ContentDetail(RetrieveAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
#
#
# class ContentUpdate(RetrieveUpdateAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#
#
# class ContentDestroy(RetrieveDestroyAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filterset_fields = ['status', 'author__username']
    search_fields = ['=title','title', 'author__username', 'description']
    ordering_fields = ['status','title']


    # def get_queryset(self):
    #
    #     queryset = Content.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     return queryset

    def get_permissions(self):

        if self.action == ['list', 'create']:
            permission_classes = [IsStafOrReadOnly]
        else:
            permission_classes = [IsStafOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]



# class UserList(ListCreateAPIView):
#     def get_queryset(self):
#         print(self.request.user)
#         print(self.request.auth)
#         return User.objects.all()
#
#     # queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class RetrieveUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
