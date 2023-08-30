# Generated by Django 4.2.4 on 2023-08-30 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('adress', models.TextField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('inn', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('series', models.IntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('term', models.DateField(auto_now_add=True)),
                ('entry_price', models.FloatField(blank=True, null=True)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('bar_code', models.ImageField(upload_to='product/bar_code/')),
                ('min_count', models.IntegerField(blank=True, null=True)),
                ('commentary', models.TextField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_branch', to='product.branch')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_category', to='product.category')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_measure', to='product.measure')),
                ('produser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_producer', to='product.producer')),
            ],
        ),
        migrations.CreateModel(
            name='StatusProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, choices=[('ready', 'Tayyor'), ('being_prepared', 'Tayyorlanmoqda'), ('not_available', 'Mavjud emas')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='SaledProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_product', models.ImageField(blank=True, null=True, upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saled_product', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_status', to='product.statusproduct'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_subcategory', to='product.subcategory'),
        ),
    ]
