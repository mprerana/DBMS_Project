# Generated by Django 2.1.7 on 2019-05-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0016_auto_20190502_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='83BA7DDF1B21', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADDCF3A38767', max_length=14),
        ),
    ]