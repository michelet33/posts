from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from core.models import Post
from core.serializers import PostSerializer
from rest_framework.response import Response


class PostAPIView(APIView):
    """
    get:
        Return a list of all post.

    post:
        Create a new post.
    """

    @swagger_auto_schema(
        operation_description="Return all posts",
        operation_summary="get all a post",
        tags=['all posts']
    )
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Return all posts",
        operation_summary="get all a post",
        tags=['all posts']
    )
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="create a new post",
        operation_summary="add a post",
        # request_body is used to specify parameters
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title', 'description'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        tags=['my post']
    )
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
