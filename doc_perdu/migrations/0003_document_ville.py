# Generated by Django 3.2.3 on 2022-01-21 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc_perdu', '0002_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='ville',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doc_perdu.ville'),
            preserve_default=False,
        ),
    ]
