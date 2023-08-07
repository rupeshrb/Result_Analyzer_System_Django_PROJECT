# Generated by Django 4.0.3 on 2022-04-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0007_user_delete_cosem3'),
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('ENROLLMENT_NO', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('SEAT_NO', models.IntegerField(max_length=10)),
                ('BRANCH', models.CharField(max_length=50)),
                ('OOP', models.CharField(max_length=300)),
                ('OPP_P', models.CharField(max_length=10)),
                ('DSU', models.CharField(max_length=10)),
                ('DSU_P', models.CharField(max_length=10)),
                ('CG', models.CharField(max_length=10)),
                ('CG_P', models.CharField(max_length=10)),
                ('DMS', models.CharField(max_length=10)),
                ('DMS_P', models.CharField(max_length=10)),
                ('DT', models.CharField(max_length=10)),
                ('DT_P', models.CharField(max_length=10)),
                ('PERCENTAGE', models.FloatField(max_length=50)),
                ('TOTAL', models.IntegerField(max_length=4)),
                ('DIST', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'COSEM2',
            },
        ),
        migrations.AlterModelTable(
            name='user',
            table='COSEM3',
        ),
    ]