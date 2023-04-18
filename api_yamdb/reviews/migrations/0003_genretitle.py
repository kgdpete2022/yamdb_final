# Generated by Django 3.2 on 2023-01-14 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.genre', verbose_name='Жанр')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.title', verbose_name='произведение')),
            ],
            options={
                'verbose_name': 'Соответствие жанра и произведения',
                'verbose_name_plural': 'Таблица соответствия жанров и произведений',
                'ordering': ('id',),
            },
        ),
    ]
