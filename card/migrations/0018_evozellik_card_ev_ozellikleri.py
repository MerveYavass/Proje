# Generated by Django 4.2 on 2023-05-24 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0017_remove_sepet_card_remove_sepet_owner_delete_favori_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvOzellik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='ev_ozellikleri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='card.evozellik'),
        ),
    ]
