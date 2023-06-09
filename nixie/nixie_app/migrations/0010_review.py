# Generated by Django 4.0.4 on 2023-05-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nixie_app', '0009_remove_product_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(db_index=True, max_length=50, verbose_name='Фамилия')),
                ('review_text', models.CharField(db_index=True, max_length=200, verbose_name='Отзыв')),
                ('available', models.BooleanField(default=False, verbose_name='Доступно')),
            ],
        ),
    ]
