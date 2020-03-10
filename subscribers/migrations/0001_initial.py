# Generated by Django 3.0.4 on 2020-03-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Email address', max_length=40)),
                ('full_name', models.CharField(help_text='First+Last Name', max_length=100)),
            ],
        ),
    ]