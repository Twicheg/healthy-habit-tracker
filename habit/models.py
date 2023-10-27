from django.db import models


class Habit(models.Model):
    periodicity = (
        ('раз в час', "once an hour"),
        ('раз в день', 'once a day'),
        ('раз в неделю', 'once a week')
    )

    user = models.CharField(max_length=50, verbose_name='user')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.DateTimeField(auto_created=False, verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    sign_of_a_pleasant_habit = models.BooleanField(default=0, verbose_name='признак приятной привычки', null=True,
                                                   blank=True)
    related_habit = models.BooleanField(default=0, verbose_name='Связанная привычка', null=True, blank=True)
    periodicity = models.CharField(max_length=20, choices=periodicity, verbose_name='переодичность',
                                   default='once a day')
    reward = models.CharField(max_length=50, verbose_name='награда', null=True, blank=True)
    time_to_complete = models.TimeField(default=0, verbose_name="время на выполнение")
    sign_of_publicity = models.BooleanField(default=0, verbose_name='признак публичности')
    related_habit_fk = models.ForeignKey("habit.Habit", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'юзер:{self.user} действие:{self.action} признак {self.sign_of_a_pleasant_habit if self.sign_of_a_pleasant_habit else self.related_habit}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
