# Generated by Django 5.0.3 on 2024-04-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('task_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
            ],
        ),
    ]