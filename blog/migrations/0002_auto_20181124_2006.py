# Generated by Django 2.0.4 on 2018-11-25 02:06

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
