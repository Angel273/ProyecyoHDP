# Generated by Django 3.2.19 on 2023-06-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230529_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='parrafo',
            name='nombre',
            field=models.CharField(default='parrafo', max_length=15),
        ),
    ]