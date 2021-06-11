# Staff program

Онлайн каталог сотрудников для компании.

#### Установка

1. Создать рабочий каталог на жестком диске.

2. Открыть рабочий каталог в терминале.

3. Ввести команду:

   ```bash
   git clone https://github.com/serg-lubeshko/staffdjango.git
   ```


4. Запустить проект в IDE (например PyCharm ) .

5. Создать виртуальную среду.

6. В окне терминала IDE для установки необходимых пакетов ввести команду:

   ```python
   pip install -r requirements.txt
   ```

#### Краткое описание проекта.

В проекте использована встроенная СУБД SQLite. С целью проверки работы она заполнена данными и не включена в .gitignore.

Проект состоит из 4 рабочих таблиц:

- таблица Position - содержит должности сотрудников;
- таблица Staff - содержит список сотрудников;
- таблица Wage - хранит данные о начисленной ЗП;
- таблица GradePosition - хранит уровни иерархий (Грейды);

Функция `def del_wage` в файле admin.py:

```python
def del_wage(modeladmin, request, queryset):
    for obj in queryset:
        obj.wages.all().delete()
```

удаляет всю информацию о выплаченной заработной плате всех выбранных сотрудников.

Функция `def redirect_staff` в admin.py:

```python
    def redirect_staff(self, obj):
    url = f"/admin/staff/staff/{obj.staffs_id}/change"
    return format_html('<a href="{}">{}</a>', url, obj.staffs)
```

формирует ссылку на объект руководителя.

Функция `def redirect_staff` в admin.py:

```python
    def fullname(self, obj):
    return '{} {} {}'.format(obj.surname, obj.name, obj.patronymic)
```

выполняет "склеивание" фамилии, имени, отчества в одну строку.

Функция `def total_wage` в admin.py:

```python
    def total_wage(self, obj):
    query = Wage.objects.filter(employee=obj.id)
    num = (query.aggregate(score=Sum("sum_wage"))).get('score')
    return num
```

возвращает суммарную заработную плату сотрудника.

