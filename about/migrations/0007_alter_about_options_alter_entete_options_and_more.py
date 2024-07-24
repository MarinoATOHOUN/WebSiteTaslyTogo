# Generated by Django 4.2.7 on 2024-06-13 09:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0006_form_img"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about",
            options={"ordering": ["nom"]},
        ),
        migrations.AlterModelOptions(
            name="entete",
            options={"ordering": ["titre"]},
        ),
        migrations.AlterModelOptions(
            name="evenements",
            options={"ordering": ["date"]},
        ),
        migrations.AlterModelOptions(
            name="exploits",
            options={"ordering": ["nbr"]},
        ),
        migrations.AlterModelOptions(
            name="podcasts",
            options={"ordering": ["nom_animateur"]},
        ),
        migrations.AlterModelOptions(
            name="tutos",
            options={"ordering": ["nom_animateur"]},
        ),
        migrations.AlterModelOptions(
            name="why_us",
            options={"ordering": ["titre"]},
        ),
    ]