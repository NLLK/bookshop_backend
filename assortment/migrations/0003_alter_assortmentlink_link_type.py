# Generated by Django 4.1.7 on 2023-03-11 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assortment', '0002_assortmentlink_alter_assortment_audio_length_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assortmentlink',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assortment.assortmenttype'),
        ),
    ]