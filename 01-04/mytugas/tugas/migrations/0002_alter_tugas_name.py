# Generated by Django 3.2.8 on 2021-10-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='name',
            field=models.TextField(),
        ),
    ]