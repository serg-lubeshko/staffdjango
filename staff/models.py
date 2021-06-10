from django.db import models

from django.db.models import Sum


class Position(models.Model):
    positions = models.CharField(max_length=50, verbose_name='Должность', unique=True)

    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.positions


class Staff(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    employment_date = models.DateField(verbose_name="Дата трудоустройства")
    wage = models.PositiveSmallIntegerField(verbose_name="Оклад")
    posit = models.ForeignKey(Position, on_delete=models.PROTECT, blank=True, null=True, related_name='posit',
                              verbose_name="Должность")
    staffs = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True, verbose_name='Руководитель')
    level = models.ForeignKey('GradePosition', on_delete=models.PROTECT, related_name='levels', blank=True, null=True,
                              verbose_name='Грейд')

    class Meta:

        verbose_name = "сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.surname} {self.name}"

class Wage(models.Model):
    date_wage = models.DateField(verbose_name="Дата начисления ЗП")
    sum_wage = models.PositiveSmallIntegerField(verbose_name="Сумма ЗП")
    employee = models.ForeignKey(Staff, on_delete=models.PROTECT, related_name="wages")

    class Meta:
        verbose_name = "Заработная плата"
        verbose_name_plural = "заработная плата"


    def __str__(self):
        return f"{self.date_wage}: {self.sum_wage} BYN"


class GradePosition(models.Model):
    grade = models.CharField(max_length=50, verbose_name='Грейд')

    class Meta:
        verbose_name = "грейд"
        verbose_name_plural = "Грейды"

    def __str__(self):
        return self.grade
