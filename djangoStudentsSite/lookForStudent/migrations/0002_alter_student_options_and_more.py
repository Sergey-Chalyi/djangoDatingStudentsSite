# Generated by Django 4.2.1 on 2024-10-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookForStudent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='time_update',
            new_name='changed_time',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='time_create',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.TextField(default='bachelor', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.TextField(default='__', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.TextField(default='m', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.TextField(default='12345', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
