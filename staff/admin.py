from django.contrib import admin
from django.db.models import Sum
from django.utils.html import format_html

from staff.models import Staff, GradePosition, Wage, Position


def del_wage(modeladmin, request, queryset):
    for obj in queryset:
        obj.wages.all().delete()


class WageAdminInline(admin.TabularInline):
    model = Wage
    extra = 0


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'posit', 'redirect_staff', 'wage', 'total_wage']
    list_filter = ['level', 'posit']
    list_display_links = ['fullname']
    actions = [del_wage]
    del_wage.short_description = "Очистить ЗП выбранных сотрудников"

    def redirect_staff(self, obj):
        url = f"/admin/staff/staff/{obj.staffs_id}/change"
        return format_html('<a href="{}">{}</a>', url, obj.staffs)

    redirect_staff.short_description = f"Руководитель"

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
admin.site.register(Position)
