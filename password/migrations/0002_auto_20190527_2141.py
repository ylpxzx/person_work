# Generated by Django 2.0 on 2019-05-27 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='password',
            options={'ordering': ['-id'], 'verbose_name': '密码管理', 'verbose_name_plural': '密码管理'},
        ),
    ]