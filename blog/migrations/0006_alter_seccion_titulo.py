# Generated by Django 3.2.19 on 2023-06-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_parrafo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='titulo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
