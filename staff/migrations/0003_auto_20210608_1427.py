# Generated by Django 3.2.4 on 2021-06-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_wage_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', models.CharField(max_length=50, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='posit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posit', to='staff.position'),
        ),
    ]