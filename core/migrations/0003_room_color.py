# Generated by Django 2.1.1 on 2018-09-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180916_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]