# Generated by Django 2.1.7 on 2019-03-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('urlid', models.IntegerField()),
                ('short', models.BooleanField(default=False)),
                ('sqlin', models.BooleanField(default=False)),
                ('heartbl', models.BooleanField(default=False)),
                ('eternalb', models.BooleanField(default=False)),
            ],
        ),
    ]