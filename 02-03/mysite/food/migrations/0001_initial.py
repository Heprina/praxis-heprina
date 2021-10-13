# Generated by Django 3.2.8 on 2021-10-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=200)),
                ('nama', models.TextField()),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Minuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=200)),
                ('nama', models.TextField()),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_makanan', models.CharField(max_length=200)),
                ('nama_minuman', models.IntegerField()),
                ('jumlah_pesanan_makanan', models.CharField(max_length=200)),
            ],
        ),
    ]