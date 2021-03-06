# Generated by Django 3.1 on 2020-08-19 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cidade',
            fields=[
                ('idcidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='doenca',
            fields=[
                ('iddoenca', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('idhospital', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('nleitos', models.IntegerField()),
                ('cidade', models.ForeignKey(db_column='cidade', on_delete=django.db.models.deletion.CASCADE, to='proj.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='registro',
            fields=[
                ('idregistro', models.AutoField(primary_key=True, serialize=False)),
                ('dtregistro', models.DateField()),
                ('ncasos', models.IntegerField()),
                ('ninternacoes', models.IntegerField()),
                ('nmortes', models.IntegerField()),
                ('doenca', models.ForeignKey(db_column='doenca', on_delete=django.db.models.deletion.CASCADE, to='proj.doenca')),
                ('hospital', models.ForeignKey(db_column='hospital', on_delete=django.db.models.deletion.CASCADE, to='proj.hospital')),
            ],
        ),
    ]
