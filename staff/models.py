from django.db import models

from django.db.models import Sum


class Staff(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    position = models.CharField(max_length=70, verbose_name='Должность')
    employment_date = models.DateField(verbose_name="Дата трудоустройства")
    wage = models.PositiveSmallIntegerField(verbose_name="Оклад")
    staffs = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True, verbose_name='Руководитель')
    level = models.ForeignKey('GradePosition', on_delete=models.PROTECT, related_name='levels', blank=True, null=True,
                              verbose_name='Грейд')
    # total_wage = models.PositiveSmallIntegerField(verbose_name='Всего начислено', null=True, blank=True)

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.surname} {self.name}"

    # def save(self, *args, **kwargs):
    #     query = Wage.objects.filter(employee=self.id)
    #     self.total_wage = (query.aggregate(score=Sum("sum_wage"))).get('score')
    #     super(Staff, self).save()


class Wage(models.Model):
    date_wage = models.DateField(verbose_name="Дата начисления ЗП")
    sum_wage = models.PositiveSmallIntegerField(verbose_name="Сумма ЗП")
    employee = models.ForeignKey(Staff, on_delete=models.PROTECT, related_name="wages")

    class Meta:
        verbose_name = "Заработная плата"
        verbose_name_plural = "заработная плата"



# Create your models here.
class GradePosition(models.Model):
    # position = models.CharField(max_length=50, verbose_name='Должность')
    grade = models.CharField(max_length=50, verbose_name='Грейд')

    class Meta:
        verbose_name = "грейд"
        verbose_name_plural = "Грейды"

    def __str__(self):
        return self.grade
