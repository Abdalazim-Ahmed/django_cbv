# Generated by Django 4.2.7 on 2023-12-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
