# Generated by Django 3.2.5 on 2022-07-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
