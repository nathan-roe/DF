# Generated by Django 4.0.6 on 2022-08-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationitem',
            old_name='cost',
            new_name='estimated_cost',
        ),
        migrations.AddField(
            model_name='donationitem',
            name='actual_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='donationitem',
            name='link_to_item',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donationitem',
            name='reason',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
