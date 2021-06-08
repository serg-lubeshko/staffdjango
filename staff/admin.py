from django.contrib import admin
from django.db.models import Sum

from staff.models import Staff, GradePosition, Wage


def del_wage(modeladmin, request, queryset):
    for obj in queryset:
        obj.wages.all().delete()


class WageAdminInline(admin.TabularInline):
    model = Wage
    extra = 0


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position', 'staffs', 'wage', 'total_wage']
    list_filter = ['position', 'level']
    list_display_links = ['fullname', 'staffs']
    actions = [del_wage]

    del_wage.short_description = "Очистить ЗП выбранных сотрудников"

    def fullname(self, obj):
        return '{} {} {}'.format(obj.surname, obj.name, obj.patronymic)

    fullname.short_description = "ФИО"

    def total_wage(self, obj):
        query = Wage.objects.filter(employee=obj.id)
        num = (query.aggregate(score=Sum("sum_wage"))).get('score')
        return num

    total_wage.short_description = "Всего выплачено"  # в блокнот

    inlines = [WageAdminInline]


admin.site.register(GradePosition)
