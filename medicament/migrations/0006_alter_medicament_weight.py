# Generated by Django 4.0 on 2022-10-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0005_alter_medicament_expr_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='weight',
            field=models.PositiveIntegerField(verbose_name='Weight'),
        ),
    ]
