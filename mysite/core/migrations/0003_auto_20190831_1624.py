# Generated by Django 2.2.4 on 2019-08-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_livraria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livraria',
            name='ISBN',
            field=models.IntegerField(),
        ),
    ]
