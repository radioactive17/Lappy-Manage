# Generated by Django 4.1.7 on 2023-04-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudapp", "0009_alter_d_laptop_table_alter_p_laptop_table_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="d_laptop",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="d_laptop",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
