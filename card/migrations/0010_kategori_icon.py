# Generated by Django 4.1.5 on 2023-05-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_alter_card_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='kategori_icons'),
        ),
    ]