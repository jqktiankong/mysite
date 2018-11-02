# Generated by Django 2.1.2 on 2018-10-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181015_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmithBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(limit_choices_to={'name_endswith': '四'}, to='blog.Author')),
            ],
        ),
    ]
