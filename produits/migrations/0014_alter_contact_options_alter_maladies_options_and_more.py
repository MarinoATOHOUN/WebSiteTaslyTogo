# Generated by Django 4.2.7 on 2024-06-13 09:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("produits", "0013_alter_contact_numero_telephone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["nom"]},
        ),
        migrations.AlterModelOptions(
            name="maladies",
            options={"ordering": ["nom"]},
        ),
        migrations.AlterModelOptions(
            name="produits",
            options={"ordering": ["date"]},
        ),
    ]