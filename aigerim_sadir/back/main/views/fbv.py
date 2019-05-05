from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import *
from ..serializers import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        
        if post.created_by==request.user:
            serializer = PostSerializer(instance=post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        if post.created_by==request.user:
            post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def put_like(request, pk):
    permission_classes = (IsAuthenticated,)
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        post.like_count+=1
        post.save()
        return Response(post.to_json())
   