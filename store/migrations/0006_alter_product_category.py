# Generated by Django 3.2.6 on 2021-08-07 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]