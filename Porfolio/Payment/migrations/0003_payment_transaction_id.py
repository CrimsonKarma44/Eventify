# Generated by Django 4.2.1 on 2023-06-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_payment_phone_no_payment_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='transaction_id',
            field=models.BigIntegerField(default=None, verbose_name='Transaction Id'),
            preserve_default=False,
        ),
    ]
