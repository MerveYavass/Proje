# Generated by Django 4.1.5 on 2023-05-30 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card', '0030_card_evsahibi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='evsahibi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profil',
            name='profilresim',
            field=models.FileField(blank=True, default='img/avatar.webp', upload_to='profilpic/'),
        ),
    ]
