# Generated by Django 4.1.5 on 2023-05-20 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0015_banyo_donanim_emniyet_konum_misafir_girisi_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={},
        ),
        migrations.RemoveField(
            model_name='card',
            name='airbnb_plus',
        ),
        migrations.RemoveField(
            model_name='card',
            name='aninda_rezervasyon',
        ),
        migrations.RemoveField(
            model_name='card',
            name='banyo_sayisi',
        ),
        migrations.RemoveField(
            model_name='card',
            name='banyolar',
        ),
        migrations.RemoveField(
            model_name='card',
            name='donanimlar',
        ),
        migrations.RemoveField(
            model_name='card',
            name='emniyetler',
        ),
        migrations.RemoveField(
            model_name='card',
            name='kendi_kendi_giris',
        ),
        migrations.RemoveField(
            model_name='card',
            name='konumlar',
        ),
        migrations.RemoveField(
            model_name='card',
            name='misafir_girisi',
        ),
        migrations.RemoveField(
            model_name='card',
            name='ozellikler',
        ),
        migrations.RemoveField(
            model_name='card',
            name='super_ev_sahibi',
        ),
        migrations.RemoveField(
            model_name='card',
            name='temel_olanaklar',
        ),
        migrations.RemoveField(
            model_name='card',
            name='yatak_odasi',
        ),
        migrations.RemoveField(
            model_name='card',
            name='yatak_sayisi',
        ),
        migrations.RemoveField(
            model_name='card',
            name='yer_tipi',
        ),
        migrations.DeleteModel(
            name='Banyo',
        ),
        migrations.DeleteModel(
            name='Donanim',
        ),
        migrations.DeleteModel(
            name='Emniyet',
        ),
        migrations.DeleteModel(
            name='Konum',
        ),
        migrations.DeleteModel(
            name='Misafir_Girisi',
        ),
        migrations.DeleteModel(
            name='Ozellikler',
        ),
        migrations.DeleteModel(
            name='TemelOlanaklar',
        ),
        migrations.DeleteModel(
            name='YatakOdasi',
        ),
    ]