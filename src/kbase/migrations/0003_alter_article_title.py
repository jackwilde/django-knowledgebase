# Generated by Django 5.1.2 on 2024-10-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbase', '0002_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]