# Generated by Django 4.2.3 on 2023-07-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
