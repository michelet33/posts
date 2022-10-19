from rest_framework.views import APIView

from core.models import Post
from core.serializers import PostSerializer
from rest_framework import response


class PostAPIView(APIView):
    """
    retrieve:
        Return the given post.

    list:
        Return a list of all post.

    create:
        Create a new post.

    destroy:
        Delete a post.

    update:
        Update a post.

    partial_update:
        Update a post.
    """
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(serializer.data)
