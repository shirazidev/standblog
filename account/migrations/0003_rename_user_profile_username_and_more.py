# Generated by Django 4.2.7 on 2023-12-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_nationalcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationalcode',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
