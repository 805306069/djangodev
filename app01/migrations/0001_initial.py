# Generated by Django 4.1.7 on 2023-03-22 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserauthInfo',
            fields=[
                ('ids', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('user_id', models.CharField(blank=True, max_length=64, null=True)),
                ('rolename', models.CharField(help_text='用户权限', max_length=16, verbose_name='用户权限')),
                ('userDisplayName', models.TextField(help_text='最后修改人', max_length=32, verbose_name='最后修改人')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('ids', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(help_text='help-pass', max_length=64, verbose_name='密码')),
                ('age', models.IntegerField()),
                ('user_id', models.CharField(blank=True, max_length=64, null=True)),
                ('basedate_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_liter', models.CharField(max_length=16)),
                ('UserInfo', models.ForeignKey(help_text='所属用户', on_delete=django.db.models.deletion.CASCADE, to='app01.userinfo', verbose_name='所属用户')),
            ],
            options={
                'db_table': 'tb_app01depart',
            },
        ),
    ]
