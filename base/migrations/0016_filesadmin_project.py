# Generated by Django 3.2.5 on 2022-07-29 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_filesadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesadmin',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.projectlanguage'),
            preserve_default=False,
        ),
    ]
