# Generated by Django 4.1.5 on 2023-05-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_card_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='card.kategori'),
        ),
    ]
