# Generated by Django 4.0.6 on 2022-08-02 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rest_framework.authentication


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('df_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverificationtoken',
            options={'default_related_name': 'email_verification_token'},
        ),
        migrations.AlterField(
            model_name='emailverificationtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ExpiringTokenAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.CharField(max_length=80)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'expiring_token',
            },
            bases=(rest_framework.authentication.TokenAuthentication, models.Model),
        ),
    ]
