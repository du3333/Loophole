# Generated by Django 2.1.7 on 2019-06-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='urls',
        #     name='dns',
        #     field=models.BooleanField(default=False),
        # ),
        migrations.AlterField(
            model_name='urls',
            name='urlid',
            field=models.CharField(max_length=45),
        ),
    ]
