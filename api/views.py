from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .tasks import send_welcome_email 

class PublicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a public endpoint."})


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}. You accessed a protected endpoint."})

class TriggerEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', 'TestUser')
        send_welcome_email.delay(username)  # call the Celery task asynchronously
        return Response({"message": f"Email will be sent to {username} in background."})
