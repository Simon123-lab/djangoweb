# Generated by Django 3.2.4 on 2021-07-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_email', models.CharField(max_length=100)),
                ('client_password', models.CharField(max_length=50)),
            ],
        ),
    ]
