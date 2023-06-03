# Generated by Django 4.2 on 2023-05-26 07:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0019_remove_card_resim_card_resim1_card_resim2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]