# Generated by Django 4.0.2 on 2022-04-18 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='outputcash',
            name='cashier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_cashier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='outputcash',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.paymenttype'),
        ),
        migrations.AddField(
            model_name='outputcash',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inputcash',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.cashbox'),
        ),
        migrations.AddField(
            model_name='inputcash',
            name='cashier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_cashier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inputcash',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.paymenttype'),
        ),
        migrations.AddField(
            model_name='inputcash',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cashbox',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.organization'),
        ),
    ]
