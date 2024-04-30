from .views import CallStateView, TaskView
from django.urls import path

urlpatterns = [
    path('call-state/', CallStateView.as_view(), name='call-state'),
    path('task/', TaskView.as_view(), name='task'),
]