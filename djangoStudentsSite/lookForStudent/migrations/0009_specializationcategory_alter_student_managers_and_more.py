# Generated by Django 4.2.1 on 2024-10-03 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookForStudent', '0008_alter_student_managers_alter_student_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecializationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lookForStudent.specializationcategory'),
        ),
    ]
