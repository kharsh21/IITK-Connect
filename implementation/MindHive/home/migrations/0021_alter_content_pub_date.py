# Generated by Django 4.0.3 on 2022-03-17 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_content_options_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 17, 16, 30, 318189), verbose_name='date published'),
        ),
    ]
