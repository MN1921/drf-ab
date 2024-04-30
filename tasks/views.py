from rest_framework import generics, status
from rest_framework.response import Response
from tasks.models import CallState, Task
from tasks.serializers import CallStateSerializer, TaskSerializer


class CallStateView(generics.ListAPIView):
    queryset = CallState.objects.all()
    serializer_class = CallStateSerializer

    def post(self, request, *args, **kwargs):
        self.create_task(request)
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

    def create_task(self, request):
        # print('!!!', request)
        _request = request
        _request.data._mutable = True
        _request.data["title"] = "Позвонить завтра"
        _request.data["description"] = "создан автоматически"
        _request.data["task_type"] = "call"
        _ = TaskView.post(request=_request)


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @staticmethod
    def post(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
