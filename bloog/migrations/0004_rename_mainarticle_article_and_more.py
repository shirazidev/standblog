# Generated by Django 4.2.7 on 2023-12-08 15:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bloog', '0003_mainarticle_maincategory_delete_article_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MainArticle',
            new_name='Article',
        ),
        migrations.RenameModel(
            old_name='MainCategory',
            new_name='Category',
        ),
    ]