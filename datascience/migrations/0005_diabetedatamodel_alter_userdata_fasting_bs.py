# Generated by Django 5.1.4 on 2024-12-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascience', '0004_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabeteDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('skin_thickness', models.IntegerField()),
                ('insulin', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('diabete_pf', models.FloatField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='fasting_bs',
            field=models.IntegerField(),
        ),
    ]
