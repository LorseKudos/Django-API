# Generated by Django 2.2.1 on 2019-06-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('comment_count', models.PositiveIntegerField(default=0)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('parent_post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_post.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_post.User')),
            ],
            options={
                'ordering': ('posted_at',),
            },
        ),
    ]
