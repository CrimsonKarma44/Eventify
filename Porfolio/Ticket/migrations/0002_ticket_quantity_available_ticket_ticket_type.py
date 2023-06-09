# Generated by Django 4.2.1 on 2023-06-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='quantity_available',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
