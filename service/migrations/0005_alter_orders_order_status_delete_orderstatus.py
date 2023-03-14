# Generated by Django 4.1.7 on 2023-03-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_quotes_moderated_alter_review_moderated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.SmallIntegerField(choices=[(0, 'New'), (50, 'Packaged'), (70, 'In Delivery'), (100, 'Closed'), (101, 'Closed Refund')], default=0),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]
