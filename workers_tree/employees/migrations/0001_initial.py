# Generated by Django 4.1.2 on 2022-10-30 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.TextField(max_length=20)),
                ('employment_date', models.DateTimeField()),
                ('salary', models.IntegerField()),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_query_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
