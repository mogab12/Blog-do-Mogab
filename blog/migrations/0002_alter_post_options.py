# Generated by Django 4.2.16 on 2024-11-13 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-data_postagem']},
        ),
    ]
