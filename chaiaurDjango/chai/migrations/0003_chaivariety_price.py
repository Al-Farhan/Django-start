# Generated by Django 5.0.6 on 2024-05-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivariety_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]