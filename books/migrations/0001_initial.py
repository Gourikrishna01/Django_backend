# Generated by Django 4.1.13 on 2023-11-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('Author', models.CharField(default='', max_length=100)),
                ('genre', models.CharField(default='', max_length=100)),
                ('image', models.CharField(default='', max_length=1000)),
                ('publishedby', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
