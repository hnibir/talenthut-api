# Generated by Django 2.0.5 on 2018-09-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talenthut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiteractivity',
            name='is_unchanged',
        ),
        migrations.AddField(
            model_name='recruiteractivity',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recruiteractivity',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
    ]
