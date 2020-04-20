# Generated by Django 3.0.5 on 2020-04-16 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtdibs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='ApprovedEvents',
        ),
        migrations.DeleteModel(
            name='Bids',
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.DeleteModel(
            name='UnapprovedEvents',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='delivery_address_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dispatch_address_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='fullname',
            field=models.CharField(blank='True', max_length=50, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='DOB',
            field=models.DateField(blank='True', null='True'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='coins',
            field=models.FloatField(blank='True', null='True'),
        ),
    ]
