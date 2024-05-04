# Generated by Django 5.0.3 on 2024-05-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_created=True)),
                ('type', models.CharField(verbose_name=20)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='shop/products/')),
            ],
        ),
    ]
