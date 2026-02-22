
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer






class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow == request.user:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response(
                {"error": "You are already following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Add to following list
        request.user.following.add(user_to_follow)

        # 🔔 Create notification
        Notification.objects.create(
            recipient=user_to_follow,
            actor=request.user,
            verb="started following you",
            content_type=ContentType.objects.get_for_model(user_to_follow),
            object_id=user_to_follow.id
        )

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )



class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
