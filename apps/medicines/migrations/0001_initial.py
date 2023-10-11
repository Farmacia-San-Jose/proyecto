# Generated by Django 4.2.6 on 2023-10-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
