# Generated by Django 2.0 on 2019-05-27 09:25

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='便签内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('image2', stdimage.models.StdImageField(upload_to='image/%Y/%m', verbose_name='图片')),
            ],
            options={
                'verbose_name': '便签',
                'verbose_name_plural': '便签',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='memo',
            name='标签',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memo.Tag'),
        ),
    ]
