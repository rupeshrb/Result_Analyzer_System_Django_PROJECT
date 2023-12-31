# Generated by Django 4.0.3 on 2022-04-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0005_result_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosem3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENROLLMENT_NO', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('SEAT_NO', models.IntegerField()),
                ('EVS', models.CharField(max_length=300)),
                ('OS', models.CharField(max_length=10)),
                ('OS_P', models.CharField(max_length=10)),
                ('AJP', models.CharField(max_length=10)),
                ('AJP_P', models.CharField(max_length=10)),
                ('ST', models.CharField(max_length=10)),
                ('ST_P', models.CharField(max_length=10)),
                ('CSSL', models.CharField(max_length=10)),
                ('CSSL_P', models.CharField(max_length=10)),
                ('IT', models.CharField(max_length=10)),
                ('PERCENTAGE', models.FloatField(max_length=10)),
                ('TOTAL', models.IntegerField()),
                ('CPP', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cosem3',
            },
        ),
    ]
