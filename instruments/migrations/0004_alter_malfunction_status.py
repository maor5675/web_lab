# Generated by Django 4.1.2 on 2022-12-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_alter_malfunction_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malfunction',
            name='status',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]
