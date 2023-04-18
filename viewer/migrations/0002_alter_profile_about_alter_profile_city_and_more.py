# Generated by Django 4.1.6 on 2023-03-20 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]