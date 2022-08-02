# Generated by Django 4.0.6 on 2022-08-01 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_recipient_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('payment_id', models.CharField(max_length=255)),
                ('payment_type', models.IntegerField(choices=[(1, 'Card'), (2, 'Paypal')], default=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='financial_donations', to='users.subscriber')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.IntegerField(choices=[(1, 'Submitted'), (2, 'Seen'), (3, 'Pending'), (4, 'Approved'), (5, 'Declined')], default=1)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donation_items', to='users.recipient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]