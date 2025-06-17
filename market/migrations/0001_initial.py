from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
from django.utils import timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('r_price', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Olish narxi')),
                ('s_price', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Sotish narxi')),
                ('stock', models.IntegerField(default=0)),
                ('start_date', models.DateField(default=timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol (arxiv emas)')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='market.sale')),
            ],
        ),
    ]

