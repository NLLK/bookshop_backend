# Generated by Django 4.1.7 on 2023-03-11 15:56

import assortment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assortment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssortmentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_type', models.SmallIntegerField()),
                ('row_link', models.FileField(upload_to=assortment.models.user_directory_path)),
            ],
        ),
        migrations.AlterField(
            model_name='assortment',
            name='audio_length_min',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.DeleteModel(
            name='AssortmentLinks',
        ),
        migrations.AddField(
            model_name='assortment',
            name='links',
            field=models.ManyToManyField(to='assortment.assortmentlink'),
        ),
    ]
