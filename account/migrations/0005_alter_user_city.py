# Generated by Django 4.1.7 on 2023-03-09 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.city'),
        ),
    ]
