# Generated by Django 3.0 on 2020-08-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('RedgNo', models.CharField(max_length=20)),
                ('CollegeName', models.CharField(max_length=100)),
                ('Interest', models.CharField(max_length=100)),
                ('Level', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=255)),
                ('Password', models.CharField(max_length=8)),
                ('ConformPassword', models.CharField(max_length=8)),
            ],
        ),
    ]