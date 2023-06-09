# Generated by Django 4.2 on 2023-05-16 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card', '0010_kategori_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('puan', models.IntegerField(default=0)),
                ('girisDate', models.DateField()),
                ('cikisDate', models.DateField()),
                ('aciklama', models.TextField(max_length=1000)),
                ('fiyat', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('resim', models.ManyToManyField(to='card.resim', verbose_name='Resimler')),
            ],
        ),
    ]
