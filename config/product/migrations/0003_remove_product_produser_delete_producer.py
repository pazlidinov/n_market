# Generated by Django 4.2.4 on 2023-09-18 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_branch_brand_rename_branch_product_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='produser',
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
