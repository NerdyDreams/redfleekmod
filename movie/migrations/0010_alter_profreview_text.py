# Generated by Django 4.0 on 2022-09-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_profreview_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profreview',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]
