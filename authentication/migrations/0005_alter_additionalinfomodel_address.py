# Generated by Django 5.0 on 2024-07-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_additionalinfomodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfomodel',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
