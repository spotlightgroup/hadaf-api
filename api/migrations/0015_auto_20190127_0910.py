# Generated by Django 2.1.5 on 2019-01-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=2),
        ),
    ]
