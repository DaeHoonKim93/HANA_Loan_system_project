# Generated by Django 3.2.9 on 2021-12-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=32, null='True', verbose_name='직원 이름')),
                ('emp_id', models.IntegerField(null='True', verbose_name='직원 번호')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '직원명단',
                'verbose_name_plural': '직원명단',
                'db_table': 'emp_list',
            },
        ),
    ]
