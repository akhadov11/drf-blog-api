from rest_framework import viewsets, permissions
from rest_framework import views, status
from rest_framework.response import Response

from core.models import Post, Comment
from core.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
        CRUD functionality for the posts.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
        CRUD functionality for the comments.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotePostView(views.APIView):
    """
        Upvoting posts.
    """

    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        post.add_upvote(user=request.user)
        return Response(status=status.HTTP_200_OK)
