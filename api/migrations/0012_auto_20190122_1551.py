# Generated by Django 2.1.5 on 2019-01-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190122_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='productImgs', to='api.Product'),
        ),
    ]
