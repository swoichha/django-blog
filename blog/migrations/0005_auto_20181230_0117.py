# Generated by Django 2.1.4 on 2018-12-30 01:17

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181228_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]
