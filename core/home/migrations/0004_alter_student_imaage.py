# Generated by Django 4.2.3 on 2023-07-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='imaage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
