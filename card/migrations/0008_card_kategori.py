# Generated by Django 4.2 on 2023-05-15 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_resim_kendi_eklediginiz_isim_alter_resim_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='card.kategori'),
        ),
    ]