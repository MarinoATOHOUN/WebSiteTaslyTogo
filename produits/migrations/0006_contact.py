# Generated by Django 4.2.7 on 2024-05-07 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("produits", "0005_delete_essaie"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("call_number", models.IntegerField(null=True)),
                (
                    "produit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="produits.produits",
                    ),
                ),
            ],
        ),
    ]