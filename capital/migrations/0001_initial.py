# Generated by Django 5.1.3 on 2024-11-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, null=True)),
                ('product_id', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ice',
            },
        ),
    ]
