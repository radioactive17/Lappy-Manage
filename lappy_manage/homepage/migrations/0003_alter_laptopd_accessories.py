# Generated by Django 4.2 on 2023-04-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0002_rename_laptop_details_laptopd_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="laptopd",
            name="accessories",
            field=models.CharField(max_length=255),
        ),
    ]
