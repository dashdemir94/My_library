# Generated by Django 3.1 on 2021-04-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Books', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('Genre', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('coments', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
