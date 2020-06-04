# Generated by Django 3.0.6 on 2020-05-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_email', models.CharField(max_length=200)),
                ('client_address', models.CharField(max_length=200)),
                ('client_phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
            ],
        ),
    ]