# Generated by Django 5.1.5 on 2025-02-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0004_delete_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Icon Class'),
        ),
    ]
