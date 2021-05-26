# Generated by Django 3.1.4 on 2021-05-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('id_proof', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('con_password', models.CharField(max_length=50)),
            ],
        ),
    ]