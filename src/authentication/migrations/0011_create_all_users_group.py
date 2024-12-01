# Generated by Django 5.1.2 on 2024-11-19 16:16

def create_all_users_group(apps, schema_editor):
    group = apps.get_model('authentication', 'Group')
    group.objects.get_or_create(id=1, defaults={'name': 'all users'})

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_user_groups_group_users_alter_group_name'),
    ]

    operations = [
        migrations.RunPython(create_all_users_group),
    ]
