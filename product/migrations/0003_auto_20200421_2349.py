# Generated by Django 2.2.4 on 2020-04-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Erkek'), ('woman', 'Kadin'), ('unisex', 'Unisex')], default='unisex', max_length=6),
        ),
    ]