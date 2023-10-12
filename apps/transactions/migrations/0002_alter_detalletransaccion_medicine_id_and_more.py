# Generated by Django 4.2.6 on 2023-10-12 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicines', '0002_historialmedicamento'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalletransaccion',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='medicines.medicamento'),
        ),
        migrations.AlterField(
            model_name='detalletransaccion',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.historialtransaccion'),
        ),
        migrations.AlterField(
            model_name='historialtransaccion',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]