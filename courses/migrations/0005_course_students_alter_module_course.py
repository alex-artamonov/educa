# Generated by Django 4.1.13 on 2023-12-23 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0004_alter_course_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                blank=True, related_name="courses_joined", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="module",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modules",
                to="courses.course",
            ),
        ),
    ]
