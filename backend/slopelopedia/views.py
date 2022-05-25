from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from authentication.models import User
from .serializers import CommentSerializer
from .serializers import ReplySerializer 
from .serializers import LocationSerializer
from .models import Location
from .models import Comment
from .models import Reply


# Location API calls

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_locations_list(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_create_location(request):
    print('User', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Comment API calls

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_comment_detail(request):
    print('User', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_by_location_id(request, location_id):       
    if request.method == 'GET':
        comments = Comment.objects.filter(location_id=location_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data) 

# Replies  API calls 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_replies_detail(request):
    print('User', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def replies_by_comment_id(request, comment_id):
    replies = Reply.objects.filter(comment_id=comment_id)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Location Likes and Dislikes API calls
# Likes and dislikes wont need body information for postman testing

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_likes_location(request, pk):
    user_likes = Location.objects.get(pk=pk)
    user_likes.likes = user_likes.likes + 1 
    serializer = LocationSerializer(user_likes, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_dislikes_location(request, pk):
    user_dislikes = Location.objects.get(pk=pk)
    user_dislikes.dislikes = user_dislikes.dislikes + 1 
    serializer = LocationSerializer(user_dislikes, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

