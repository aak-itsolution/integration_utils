# Generated by Django 3.2.23 on 2024-05-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix24', '0005_alter_bitrixuser_id_alter_bitrixusertoken_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitrixuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bitrixusertoken',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
