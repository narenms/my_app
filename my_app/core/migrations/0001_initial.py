# Generated by Django 3.0.8 on 2020-07-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100)),
                ('phone_no', models.CharField(blank=True, max_length=300)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
