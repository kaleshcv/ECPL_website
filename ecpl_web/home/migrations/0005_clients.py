# Generated by Django 3.1.2 on 2020-10-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/logos')),
            ],
        ),
    ]
