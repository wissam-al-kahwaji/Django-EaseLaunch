from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import generics
from apps.utils.permissions import MePermission
from apps.accounts.serializers import UserSerializer, UserStatusAuth


class Me(generics.GenericAPIView):
    """
    API view to fetch the user's personal data and check authentication status.
    """

    permission_classes = [MePermission]

    def get_serializer(self, *args, **kwargs):
        if self.request.method in "POST":
            return UserStatusAuth()
        if self.request.method in "GET":
            return UserSerializer()

    @extend_schema(
        operation_id="Me",
        summary="Fetch user's personal data",
        responses=UserSerializer,
    )
    def get(self, request):
        """
        Fetch the authenticated user's personal data.

        This endpoint retrieves and returns the personal data of the authenticated user.
        """
        user_serializer = UserSerializer(request.user)
        return Response(user_serializer.data)

    @extend_schema(
        operation_id="Me Status",
        summary="Check if the user is authenticated",
        request=None,
    )
    def post(self, request, *args, **kwargs):
        """
        Check the user's authentication status.

        This endpoint checks if the user is logged in and returns the authentication status.
        """
        return Response(UserStatusAuth({"status": request.user.is_authenticated}).data)