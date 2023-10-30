from django.db import models


class Habit(models.Model):
    owner = models.ForeignKey('users.User', verbose_name='owner', on_delete=models.CASCADE, null=True, blank=True)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(auto_created=False, verbose_name='время', null=True, blank=True)
    action = models.CharField(max_length=100, verbose_name='действие')
    sign_of_a_pleasant_habit = models.BooleanField(default=0, verbose_name='признак приятной привычки', null=True,
                                                   blank=True)
    related_habit = models.ForeignKey("habit.Habit", null=True, blank=True, on_delete=models.CASCADE)
    periodicity_in_week = models.SmallIntegerField(verbose_name='переодичность в неделю ', )
    reward = models.CharField(default=None, max_length=50, verbose_name='награда', null=True, blank=True)
    time_to_complete = models.IntegerField(default=0, verbose_name="время на выполнение",
                                           null=True, blank=True)
    is_public = models.BooleanField(default=0, verbose_name='признак публичности')
    last_send = models.DateTimeField(default=None, null=True, blank=True,
                                     verbose_name="время последней отправки напоминания")

    def __str__(self):
        return f'юзер:{self.owner} действие:{self.action} признак {self.sign_of_a_pleasant_habit if self.sign_of_a_pleasant_habit else self.related_habit}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
