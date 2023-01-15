# Generated by Django 4.1.2 on 2023-01-12 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0009_handled_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='handled_by',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instruments.malfunction'),
            preserve_default=False,
        ),
    ]
