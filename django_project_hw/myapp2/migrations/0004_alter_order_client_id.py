# Generated by Django 5.0.4 on 2024-04-09 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_alter_order_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.client'),
        ),
    ]