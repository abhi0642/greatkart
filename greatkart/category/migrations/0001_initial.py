# Generated by Django 3.2.9 on 2021-11-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=700)),
                ('cat_image', models.ImageField(blank=True, upload_to='photoes/category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Catogories',
            },
        ),
    ]
