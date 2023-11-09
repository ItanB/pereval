from django.shortcuts import render
import django_filters
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins, generics
from .serializers import *
from .models import *


class SubmitData(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['users__email']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED, 'message': 'Запись создана', 'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': serializer.errors})


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class PerevalAddedViewSet(viewsets.ModelViewSet):
    serializer_class = PerevalAddedSerializer
    queryset = PerevalAdded.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('users__email',)
    http_method_names = ['get', 'post', 'head', 'patch', 'options']

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успешно',
                    'id': None
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка 500',
                    'id': None
                }
            )

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalAddedSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Изменения сохранены'
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'Текущий статус: {pereval.get_status_display()}, данные не могут быть изменены!'
                }
            )

    def get_queryset(self):
        queryset = PerevalAdded.objects.all()
        pereval_id = self.request.query_params.get('users_id', None)
        users_id = self.request.query_params.get('users_id', None)
        if pereval_id is not None:
            queryset = queryset.filter(users_id=users_id)
            return queryset
