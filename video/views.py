from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def video_upload_view(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def subtitles_view(request):
    try:
        videos = Video.objects.all()
    except Video.DoesNotExist:
        return Response(status=404)

    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


