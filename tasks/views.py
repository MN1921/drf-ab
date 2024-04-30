from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from tasks.models import CallState, Task
from tasks.serializers import CallStateSerializer, TaskSerializer
from rest_framework.decorators import api_view


class CallStateView(generics.ListAPIView):
    queryset = CallState.objects.all()
    serializer_class = CallStateSerializer

    def post(self, request, *args, **kwargs):
        serializer = CallStateSerializer(data=request.data)
        if serializer.is_valid():

    # второй вариант реализации отсутствия причины при звонке
    #         task_type = request.data.get('call')
    #         result = request.data.get('result')
    #         reason = request.data.get('reason')
    #
    #         if task_type == task_type:
    #             if result == 'unsuccessful' and not reason:
    #                 raise ValidationError('Необходимо указать причину неуспешного результата звонка')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

