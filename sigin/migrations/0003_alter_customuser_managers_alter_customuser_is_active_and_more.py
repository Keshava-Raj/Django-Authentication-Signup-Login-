# Generated by Django 5.1.4 on 2025-01-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigin', '0002_remove_customuser_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
