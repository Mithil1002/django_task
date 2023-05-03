from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Work, Client
from .serializers import WorkSerializer


@api_view(['GET'])
def apis(request):
    routes = [
        'GET/api/works',
        'GET/api/works?work_type=',
        'GET/api/work?artist=',
        'GET/api/register',

    ]
    return Response(routes)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    Client.objects.create(user=user, name=username)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def work_list(request):
    work_type = request.query_params.get('work_type', None)
    artist = request.query_params.get('artist', None)

    if work_type is not None:
        queryset = Work.objects.filter(work_type__icontains=work_type)

    elif artist is not None:
        queryset = Work.objects.filter(artist__name__icontains=artist)

    else:
        queryset = Work.objects.all()

    serializer = WorkSerializer(queryset, many=True)
    return Response(serializer.data)
