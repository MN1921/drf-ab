from rest_framework import serializers
from tasks.models import CallState, Task


class CallStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallState
        fields = '__all__'

    def validate(self, attrs):
        print('!!!', attrs)
        task = attrs.get('task')
        result = attrs.get('result')
        reason = attrs.get('reason')

        if task.task_type == 'call':
            if result == 'unsuccessful' and not reason:
                raise serializers.ValidationError('Необходимо указать причину неуспешного результата звонка')

        return attrs


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
