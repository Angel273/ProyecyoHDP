# Generated by Django 3.2.19 on 2023-05-30 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='titulo',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
