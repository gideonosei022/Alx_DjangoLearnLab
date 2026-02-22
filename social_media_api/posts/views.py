from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from accounts.models import CustomUser


# =========================
# Post ViewSet
# =========================

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# =========================
# Comment ViewSet
# =========================

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # 🔔 Notify post author when someone comments
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb="commented on your post",
                content_type=ContentType.objects.get_for_model(comment.post),
                object_id=comment.post.id
            )


# =========================
# Feed View
# =========================

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()

        # ALX required format
        return Post.objects.filter(
            author__in=following_users
        ).order_by("-created_at")


# =========================
# Like Post
# =========================

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response(
                {"error": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        Like.objects.create(user=request.user, post=post)

        # 🔔 Notify post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return Response(
            {"message": "Post liked successfully."},
            status=status.HTTP_200_OK
        )


# =========================
# Unlike Post
# =========================

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response(
                {"error": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()

        return Response(
            {"message": "Post unliked successfully."},
            status=status.HTTP_200_OK
        )
