# Generated by Django 4.0.3 on 2022-04-10 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storefront', '0002_made_rate_field_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(default='USA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('P', 'Premium'), ('N', 'Normal')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='09666', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='storefront.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='storefront.product')),
            ],
        ),
    ]