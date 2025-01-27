# Generated by Django 5.1.1 on 2024-09-21 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('access', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pub', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='pub', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
