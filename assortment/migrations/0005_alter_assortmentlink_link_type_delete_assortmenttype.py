# Generated by Django 4.1.7 on 2023-03-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assortment', '0004_alter_assortment_assortment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assortmentlink',
            name='link_type',
            field=models.SmallIntegerField(),
        ),
        migrations.DeleteModel(
            name='AssortmentType',
        ),
    ]
