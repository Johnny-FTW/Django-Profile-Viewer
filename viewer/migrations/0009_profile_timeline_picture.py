# Generated by Django 4.1.6 on 2023-06-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timeline_picture',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]