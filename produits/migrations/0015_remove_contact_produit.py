# Generated by Django 4.2.7 on 2024-06-14 17:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("produits", "0014_alter_contact_options_alter_maladies_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="produit",
        ),
    ]