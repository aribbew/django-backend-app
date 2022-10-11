# Generated by Django 4.1.1 on 2022-10-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paymentType',
            field=models.CharField(choices=[('CARD', 'card'), ('CASH', 'cash')], max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='statusPayment',
            field=models.CharField(choices=[('PENDING', 'pending'), ('PAID', 'paid')], max_length=255),
        ),
    ]
