# Generated by Django 4.1.1 on 2022-10-07 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0010_bookambulance_hname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookambulance',
            name='hname',
        ),
        migrations.AddField(
            model_name='bookambulance',
            name='hospital',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='enroll.hospital'),
            preserve_default='True',
        ),
    ]
