# Generated by Django 3.1.5 on 2021-04-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210403_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_count',
            field=models.IntegerField(default=0),
        ),
    ]
