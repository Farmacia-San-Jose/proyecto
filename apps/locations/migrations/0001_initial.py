# Generated by Django 4.2.6 on 2023-10-11 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicines', '0002_historialmedicamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_location', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialInvetario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_stock', models.IntegerField()),
                ('row', models.CharField(max_length=50)),
                ('column', models.CharField(max_length=50)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.ubicacion')),
                ('locationsection_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.seccion')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicamento')),
            ],
        ),
    ]
