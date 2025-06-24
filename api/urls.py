from django.urls import path
from .views import PublicView, ProtectedView,TriggerEmailView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('send-email/', TriggerEmailView.as_view(), name='send-email'),
]
