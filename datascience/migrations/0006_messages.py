# Generated by Django 5.1.5 on 2025-01-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascience', '0005_diabetedatamodel_alter_userdata_fasting_bs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
