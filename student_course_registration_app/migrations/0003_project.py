# Generated by Django 5.0.4 on 2024-04-07 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_course_registration_app', '0002_remove_student_name_student_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('languages_used', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField(help_text='Duration in weeks')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='student_course_registration_app.student')),
            ],
        ),
    ]
