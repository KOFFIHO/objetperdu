# Generated by Django 3.2.3 on 2022-01-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_perdu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
    ]
