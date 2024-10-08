# Generated by Django 4.2.1 on 2024-10-03 08:38

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('lookForStudent', '0007_alter_student_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'draft blank'), (1, 'published')], default=1),
        ),
    ]
