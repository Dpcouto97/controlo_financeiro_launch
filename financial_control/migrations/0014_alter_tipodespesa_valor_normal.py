# Generated by Django 4.0.5 on 2022-06-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_control', '0013_alter_tipodespesa_valor_normal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodespesa',
            name='valor_normal',
            field=models.DecimalField(decimal_places=10, default=None, max_digits=10, null=True),
        ),
    ]
