# Generated by Django 4.0.3 on 2022-03-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam_stock', '0002_pinjam_barang_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenis_barang',
            name='kode_jenis',
            field=models.CharField(max_length=10),
        ),
    ]
