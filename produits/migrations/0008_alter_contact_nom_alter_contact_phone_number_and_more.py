# Generated by Django 4.2.7 on 2024-05-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produits", "0007_rename_call_number_contact_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="nom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="contact",
            name="produit",
            field=models.CharField(max_length=100),
        ),
    ]
