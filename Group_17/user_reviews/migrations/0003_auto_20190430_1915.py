# Generated by Django 2.1.7 on 2019-04-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_reviews', '0002_auto_20190430_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
