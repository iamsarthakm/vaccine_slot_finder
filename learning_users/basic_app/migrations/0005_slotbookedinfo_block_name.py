# Generated by Django 3.2.5 on 2021-08-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_alter_slotbookedinfo_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotbookedinfo',
            name='block_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
