# Generated by Django 4.1.4 on 2023-01-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0004_alter_coindatamodel_name_alter_coindatamodel_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coindatamodel',
            name='name',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='coindatamodel',
            name='symbol',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]