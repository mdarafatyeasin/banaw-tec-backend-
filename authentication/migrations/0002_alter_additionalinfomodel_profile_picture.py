# Generated by Django 5.0 on 2024-07-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfomodel',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='profile_picture'),
        ),
    ]