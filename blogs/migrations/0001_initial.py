# Generated by Django 4.0.4 on 2022-05-01 08:43

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментраии',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tag', models.CharField(blank=True, max_length=50, null=True)),
                ('in_archive', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='ReplyToComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.post')),
            ],
            options={
                'verbose_name': 'Отвеченный Комментарий',
                'verbose_name_plural': 'Отвеченные Комментраии',
                'db_table': 'ReplyToComment',
            },
        ),
        migrations.CreateModel(
            name='ReplyToReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.post')),
                ('replied_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.replytocomment')),
            ],
            options={
                'verbose_name': 'Комментарий на отвеченный комментарий',
                'verbose_name_plural': 'Комментарии на отвеченные комментарий',
                'db_table': 'ReplyToReply',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.post'),
        ),
    ]
