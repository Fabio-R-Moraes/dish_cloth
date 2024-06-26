# Generated by Django 5.0.6 on 2024-05-15 00:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Buies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_buy', models.DateTimeField(auto_now_add=True)),
                ('note_number', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dish_Cloths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=120)),
                ('is_published', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('quantity_unit', models.CharField(max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('price_unit', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cloth_image', models.ImageField(upload_to='dish_cloth/cloth_images/%d/%m/%Y')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dish_cloth.category')),
            ],
        ),
        migrations.CreateModel(
            name='items_buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dish_cloth.dish_cloths')),
                ('note_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dish_cloth.buies')),
            ],
        ),
    ]
