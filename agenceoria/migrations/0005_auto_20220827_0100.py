# Generated by Django 2.2.10 on 2022-08-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenceoria', '0004_auto_20220826_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvresume',
            name='cv',
            field=models.FileField(upload_to='cv'),
        ),
    ]
