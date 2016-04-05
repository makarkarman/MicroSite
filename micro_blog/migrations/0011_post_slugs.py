# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def generate_blog_slugs(apps, schema_editor):
    from micro_blog.models import Post, Post_Slugs
    post_slugs = []
    for blog in Post.objects.all():
        post_slugs.append(
            Post_Slugs(blog=blog, slug=blog.slug, is_active=True)
        )
    Post_Slugs.objects.bulk_create(post_slugs)


class Migration(migrations.Migration):

    dependencies = [
        ('micro_blog', '0010_post_old_slugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Slugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slugs', to='micro_blog.Post')),
            ],
        ),
        migrations.RunPython(generate_blog_slugs),
    ]