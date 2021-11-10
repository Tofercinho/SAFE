# Generated by Django 3.2.4 on 2021-06-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproduct',
            name='gender',
            field=models.IntegerField(choices=[[0, 'male-adult'], [1, 'female-adult'], [2, 'male-boy'], [3, 'female-girl']]),
        ),
        migrations.AlterField(
            model_name='newproduct',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
