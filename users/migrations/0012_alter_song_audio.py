# Generated by Django 3.2 on 2021-04-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210426_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
