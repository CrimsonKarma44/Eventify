# Generated by Django 4.2.1 on 2023-06-08 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eventify', '0003_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start', '-end']},
        ),
    ]