# Generated by Django 4.2.15 on 2025-05-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment_is_author_reply_alter_comment_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blog",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
