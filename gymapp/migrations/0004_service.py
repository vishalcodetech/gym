# Generated by Django 4.2.5 on 2024-01-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=200)),
                ('service_title', models.CharField(max_length=200)),
                ('service_desc', models.TextField()),
            ],
        ),
    ]
