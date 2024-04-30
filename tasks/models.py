from django.db import models


class Task(models.Model):
    objects = models.Manager()
    TASK_TYPE_CHOICES = (
        ('call', 'Звонок'),
        ('appointment', 'Встреча'),
    )
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField(max_length=512, verbose_name='Описание')
    task_type = models.CharField(max_length=100, choices=TASK_TYPE_CHOICES, verbose_name='Тип задачи')

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class CallState(models.Model):
    RESULT_CHOICES = (
        ('successful', 'успешный'),
        ('unsuccessful', 'неуспешный'),
    )
    REASON_CHOICES = (
        ('reason_1', 'причина_1'),
        ('reason_2', 'причина_2'),
        ('reason_3', 'причина_3'),
    )

    task = models.OneToOneField(Task, on_delete=models.CASCADE, verbose_name='Задача')
    result = models.CharField(max_length=100, choices=RESULT_CHOICES, verbose_name='Результат звонка')
    reason = models.CharField(max_length=100, choices=REASON_CHOICES, verbose_name='Причина', blank=True, null=True)

    class Meta:
        verbose_name = 'Состояние вызова'
        verbose_name_plural = 'Состояние вызова'

    # def save(self, *args, **kwargs):
    #     if self.task.task_type != 'call':
    #         raise ValidationError('Только для звонков')

        # первый вариант реализации отсутствия причины при звонке
        # if self.task.task_type == 'call':
        #     if self.result == 'unsuccessful' and not self.reason:
        #         raise ValidationError('Необходимо указать причину неуспешного результата звонка')
        # super(CallState, self).save(*args, **kwargs)

    def __str__(self):
        return ' '.join([str(self.result), str(self.reason)])
