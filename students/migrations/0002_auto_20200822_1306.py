# Generated by Django 3.0 on 2020-08-22 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='FirstName',
            new_name='StudentName',
        ),
    ]