# Generated by Django 4.0.5 on 2022-06-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_aboutsection_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=255),
        ),
    ]
