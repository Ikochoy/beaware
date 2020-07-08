# Generated by Django 3.0.6 on 2020-06-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dislike_comments',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='member',
            name='disliked_posts',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='member',
            name='liked_comments',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AddField(
            model_name='member',
            name='liked_post',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
