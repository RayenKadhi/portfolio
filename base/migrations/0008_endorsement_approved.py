# Generated by Django 3.2.5 on 2022-07-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
