# Generated by Django 2.1.7 on 2019-04-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_auto_20190429_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='2F65A1CD4D5A', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADDCDC492D10', max_length=14),
        ),
    ]
