# Generated by Django 5.0.4 on 2024-04-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0004_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
