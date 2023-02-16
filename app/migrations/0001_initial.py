# Generated by Django 4.1.7 on 2023-02-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_title', models.TextField(verbose_name='Факт')),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты',
            },
        ),
    ]