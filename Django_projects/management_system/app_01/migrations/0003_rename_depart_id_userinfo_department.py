# Generated by Django 5.0.2 on 2024-03-09 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0002_rename_depart_userinfo_depart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='depart_id',
            new_name='department',
        ),
    ]
