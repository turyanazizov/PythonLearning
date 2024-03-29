# Generated by Django 4.0.5 on 2022-06-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0002_remove_blog_author_delete_author_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
                ('status', models.BooleanField()),
            ],
        ),
    ]
