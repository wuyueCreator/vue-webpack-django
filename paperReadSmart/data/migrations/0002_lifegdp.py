# Generated by Django 2.1.1 on 2018-09-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeGdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('json_data', models.CharField(max_length=10000, verbose_name='json数据')),
                ('create_time', models.DateTimeField(verbose_name='date create')),
            ],
        ),
    ]
