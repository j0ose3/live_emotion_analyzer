# Generated by Django 2.2 on 2019-04-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
