# Generated by Django 4.0.4 on 2023-05-12 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nixie_app', '0011_alter_review_review_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-id',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
