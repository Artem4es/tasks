# Generated by Django 3.1 on 2023-03-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(null=True, upload_to='xlsx_files', verbose_name='Файл'),
        ),
    ]