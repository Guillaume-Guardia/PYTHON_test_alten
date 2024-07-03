# Generated by Django 5.0.6 on 2024-07-03 01:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField()),
                ("inventory_status", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=100)),
                ("image", models.URLField(blank=True, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]