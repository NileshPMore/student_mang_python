# Generated by Django 5.2.1 on 2025-05-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
